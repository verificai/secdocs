from synthesize_transactions import *
import json
import os

#send_anthropic_message("Tell me a story", "You are a fantasy novelist who speaks in five word sentences.")
 
def nice_mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def process_plaintiff(plaintiff_record, plaintiff_index, plaintiff_filename_prefix):
    plaintiff_record_cleaned = select_relevant_keys(plaintiff_record)

    messages = []
    prompts = load_prompts()

    customer_prompt = prompts['customer.txt']
    customer_prompt= customer_prompt.replace("{CASE_DATA}", json.dumps(plaintiff_record_cleaned))

    customer_response = send_anthropic_message(messages, customer_prompt)

    allocation_prompt = prompts['allocation.txt']
    allocation_response = send_anthropic_message(messages, allocation_prompt)

    transactions_prompt = prompts['transactions.txt']
    transactions_response = send_anthropic_message(messages, transactions_prompt)

    print("** Customer Response: ", customer_response)
    print("** Allocation Response: ", allocation_response)
    print("** Transactions Response: ", transactions_response)

    # TODO Save the messages to a file for later use

    adjudication_prompt = prompts['adjudication.txt']

    adjudication_prompt = adjudication_prompt.replace("{CUSTOMER}", customer_response)
    adjudication_prompt = adjudication_prompt.replace("{ALLOCATION}", allocation_response)
    adjudication_prompt = adjudication_prompt.replace("{TRANSACTIONS}", transactions_response)

    adjudication_response = send_anthropic_message(messages, adjudication_prompt)
    print("** Adjudication Response: ", adjudication_response)

    nice_mkdir("./synthesize_output")

    nice_mkdir(f"./synthesize_output/{plaintiff_filename_prefix}")

    nice_mkdir(f"./synthesize_output/{plaintiff_filename_prefix}/{plaintiff_index}")
    
    with open(f"./synthesize_output/{plaintiff_filename_prefix}/{plaintiff_index}/customer_response.txt", "w") as f:
        f.write(customer_response)
    with open(f"./synthesize_output/{plaintiff_filename_prefix}/{plaintiff_index}/allocation_response.txt", "w") as f:
        f.write(allocation_response)
    with open(f"./synthesize_output/{plaintiff_filename_prefix}/{plaintiff_index}/transactions_response.txt", "w") as f:
        f.write(transactions_response)
    with open(f"./synthesize_output/{plaintiff_filename_prefix}/{plaintiff_index}/adjudication_response.txt", "w") as f:
        f.write(adjudication_response)


case_data = get_case_data()

for plaintiff_filename in case_data.keys():
    # TODO More than one plaintiff
    plaintiff_filename_prefix = plaintiff_filename.replace('.json', '')
    for plaintiff_index, plaintiff_record in enumerate(case_data[plaintiff_filename]):
        process_plaintiff(plaintiff_record, plaintiff_index, plaintiff_filename_prefix)

