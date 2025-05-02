import json
import sacrebleu
import sys
import np

lang = sys.argv[1]
with open(f'results/tscores_{lang}.json', 'r') as f:
    data = json.load(f)


for item in data:
    reference = item['Translation']
    candidate = item['Response']
    bleu = sacrebleu.sentence_bleu(candidate, [reference]).score
    item['bleu_score'] = round(bleu, 4)

with open(f'results/tscores_{lang}.json', 'w') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)




with open(f'results/tscores_{lang}_mann_ki_baat.json', 'r') as f:
    data = json.load(f)

for item in data:
    reference = item['Translation']
    candidate = item['Response']
    bleu = sacrebleu.sentence_bleu(candidate, [reference]).score
    item['bleu_score'] = round(bleu, 4)

with open(f'results/tscores_{lang}_mann_ki_baat.json', 'w') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

file_name = f'results/tscores_{lang}.json'

with open(file_name) as f:
    data = json.load(f)

# Extract all 'score' values (assuming a list of dicts)
scores = [item["Fluency"] for item in data if "Fluency" in item and item["Translation"] != ""]

# Calculate mean and standard deviation
mean_score = np.mean(scores)
std_dev_score = np.std(scores)

print(f"{file_name} Fluency: Mean: {mean_score}, Std Dev: {std_dev_score}")

# Extract all 'score' values (assuming a list of dicts)
scores = [item["Accuracy"] for item in data if "Accuracy" in item and item["Translation"] != ""]

# Calculate mean and standard deviation
mean_score = np.mean(scores)
std_dev_score = np.std(scores)

print(f"{file_name} Adequacy: Mean: {mean_score}, Std Dev: {std_dev_score}")
    
avg_bleu = 0
cnt = 0
for i in data:
    if i.get("Translation", "") != "":
        avg_bleu += i['bleu_score']  
        cnt += 1      

print(cnt)
avg_bleu /= cnt

avg_bleu = round(avg_bleu, 4)

print(f"Avg BLEU score for file {file_name} is {avg_bleu}")

file_name = f'results/tscores_{lang}_mann_ki_baat.json'

with open(file_name) as f:
    data = json.load(f)

# Extract all 'score' values (assuming a list of dicts)
scores = [item["Fluency"] for item in data if "Fluency" in item and item["Translation"] != ""]

# Calculate mean and standard deviation
mean_score = np.mean(scores)
std_dev_score = np.std(scores)

print(f"{file_name} Fluency: Mean: {mean_score}, Std Dev: {std_dev_score}")

# Extract all 'score' values (assuming a list of dicts)
scores = [item["Accuracy"] for item in data if "Accuracy" in item and item["Translation"] != ""]

# Calculate mean and standard deviation
mean_score = np.mean(scores)
std_dev_score = np.std(scores)

print(f"{file_name} Adequacy: Mean: {mean_score}, Std Dev: {std_dev_score}")
    
avg_bleu = 0
cnt = 0
for i in data:
    if i.get("Translation", "") != "":
        avg_bleu += i['bleu_score']  
        cnt += 1      

print(cnt)
avg_bleu /= cnt

avg_bleu = round(avg_bleu, 4)

print(f"Avg BLEU score for file {file_name} is {avg_bleu}")
