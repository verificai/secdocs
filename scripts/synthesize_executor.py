from synthesize_transactions import *
import json

#send_anthropic_message("Tell me a story", "You are a fantasy novelist who speaks in five word sentences.")
 
case_data = get_case_data()

# TODO More than one plaintiff
plaintiff_record = case_data['Justin_W_Pagel_2022073340901.json'][0]
plaintiff_record_cleaned = select_relevant_keys(plaintiff_record)

prompts = load_prompts()

messages = []

customer_prompt = prompts['customer.txt']
customer_prompt_replaced = customer_prompt.replace("{CASE_DATA}", json.dumps(plaintiff_record_cleaned))

customer_response = send_anthropic_message(messages, customer_prompt_replaced)

allocation_prompt = prompts['allocation.txt']
allocation_response = send_anthropic_message(messages, allocation_prompt)

transactions_prompt = prompts['transactions.txt']
transactions_response = send_anthropic_message(messages, transactions_prompt)

print("** Customer Response: ", customer_response)
print("** Allocation Response: ", allocation_response)
print("** Transactions Response: ", transactions_response)


