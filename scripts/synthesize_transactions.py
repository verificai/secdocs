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

    cases_map[filename] = data
    return cases_map

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
API_URL = "https://api.anthropic.com/v1/messages"


anthropic_client = anthropic.Anthropic(api_key=API_KEY)

def send_anthropic_message(user_message, system_message="", max_tokens=4096):
    messages = [{"role": "user", "content": user_message}]

    response = anthropic_client.messages.create(
        model="claude-3-7-sonnet-20250219",
        system=system_message,
        max_tokens=max_tokens,
        messages=messages)

    return response.content[0].text


def prepare_system_message():
    return (
        "You are a financial assistant. "
        "Your task is to help users synthesize transactions from their bank statements. "
        "Please provide a summary of the transactions in a structured format."
    )

