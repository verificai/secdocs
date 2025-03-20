# Scripts

## synthesize_executor.py

- Put Claude-generated case summaries in ../case_summaries_teddy (WILL CHANGE) 
- From this directory, python synthesize_executor.py will create:
  - synthesize_output/<CASE NAME>
  - synthesize_output/<CASE NAME>/<PLAINTIFF INDEX>
    - customer_response.txt # faked customer profile
    - allocation_response.txt # faked customer allocations
    - transactions_response.txt # faked transactions
    - adjudication_response.txt # adjudication to 24015-l ii.2../
- Prompts are in synthesize_prompts
