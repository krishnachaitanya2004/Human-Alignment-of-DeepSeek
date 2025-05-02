import pandas as pd
import json
import time
from prompt import create_prompt
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from together import Together

api_key = "YOUR_API_KEY" # 350-num_rows

client = Together(api_key=api_key)

df = pd.read_csv('filtered_complete_data.csv')
cols = df.columns
num_rows = len(df)

# FOR DEBUGGING
LIMIT_DATA_SIZE = -1 # If want to disable then set to -1
LIMIT_NUM_QUESTIONS = -1 # If want to disable then set to -1

with open('combined_questions.json') as f:
    questions = json.load(f)

if LIMIT_NUM_QUESTIONS > 0:
    questions = {k: questions[k] for k in list(questions)[:LIMIT_NUM_QUESTIONS]}  # Limit number of questions for debugging

# Retry-enabled question asker
def ask_question(qid, question, row_data, max_retries=3):
    for attempt in range(max_retries):
        try:
            prompt_text = create_prompt(row_data, question)
            cot_eval = client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V3",
                messages=[{"role": "user", "content": prompt_text}]
            )
            return qid, cot_eval.choices[0].message.content
        except Exception as e:
            wait_time = 2 ** (attempt+1)
            print(f"[{qid}] Retry {attempt+1}/{max_retries} after error: {e}")
            time.sleep(wait_time)
    return qid, f"Error after {max_retries} retries"

def process_data(i):
    try:
        row_data = df.iloc[i, :]
        results = {}
        
        for qid, question in tqdm(questions.items()):
            qid, result = ask_question(qid, question, row_data)
            results[qid] = result
            time.sleep(2) # Rate limiting

        return results
    except Exception as e:
        print(f"Error processing row {i}: {e}")
        return []


data_list = []
# Perform without threading
if LIMIT_DATA_SIZE > 0:
    num_rows = min(num_rows, LIMIT_DATA_SIZE)  # Limit number of rows for debugging
for i in tqdm(range(num_rows)):
    result = process_data(i)
    with open("outputs/"+""+str(i)+".json", 'w') as file_:
        json.dump(result, file_, indent=4)
    
    # Also dump the metadata from df
    # metadata = df.iloc[i, :].to_dict()
    # with open("outputs/"+""+str(i)+"_metadata.json", 'w') as file_:
    #     json.dump(metadata, file_, indent=4)
