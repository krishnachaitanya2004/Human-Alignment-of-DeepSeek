import json

with open('english_Toxic_scores.json','r') as f:
    english_scores = json.load(f)

score = 0

for i in range(len(english_scores)):
    score = score + english_scores[i]['Continuation Toxicity']

score = score / len(english_scores)
print("Average Toxicity Score: ", score)
