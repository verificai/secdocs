import os
import json
from dotenv import load_dotenv
import anthropic

CASES_DIR = "../cases_summaries_teddy"

def get_case_data():
    cases_map  = {}
    # Read and process each JSON file in the directory
    for filename in os.listdir(CASES_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(CASES_DIR, filename)
            with open(filepath, "r") as file:
                data = json.load(file)
        print("READING FILENAME: ", filename)
        cases_map[filename] = data
    return cases_map

# Load environment variables from .env file

API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    raise ValueError("ANTHROPIC_API_KEY is not set in the environment variables.")

anthropic_client = anthropic.Anthropic(api_key=API_KEY)

# def send_anthropic_message_raw(user_message, system_message="", max_tokens=4096):
#     messages = [{"role": "user", "content": user_message}]

#     response = anthropic_client.messages.create(
#         model="claude-3-7-sonnet-20250219",
#         system=system_message,
#         max_tokens=max_tokens,
#         messages=messages)
    
#     return response

PROMPTS_DIR = "./synthesize_prompts"
def load_prompts():
    prompts_map = {}
    # Read and process each JSON file in the directory
    for filename in os.listdir(PROMPTS_DIR):
        if filename.endswith(".txt"):
            filepath = os.path.join(PROMPTS_DIR, filename)
            with open(filepath, "r") as file:
                data = file.read()

            prompts_map[filename] = data
    return prompts_map


# Stateful (gross)
def send_anthropic_message(messages, user_message, system_message="", max_tokens=4096):
    new_user_message_record = {"role": "user", "content": user_message}

    messages.append(new_user_message_record)
    
    response = anthropic_client.messages.create(
        model="claude-3-7-sonnet-20250219",
        system=system_message,
        max_tokens=max_tokens,
        messages=messages)

    new_assistant_message_record =  {"role": "assistant", "content": response.content[0].text}
    messages.append(new_assistant_message_record)
    return messages[-1]['content'] # convenience



def select_relevant_keys(plaintiff_record):
    relevant_keys = [
    "Demographics", 
    "InvestmentType",
    "Account Information"
    "FinancialLossSuffered"
    ]

    filtered_record = {key: plaintiff_record[key] for key in relevant_keys if key in plaintiff_record }
    return filtered_record


def prepare_system_message():
    return (
        "You are a financial assistant. "
        "Your task is to help users synthesize transactions from their bank statements. "
        "Please provide a summary of the transactions in a structured format."
    )

