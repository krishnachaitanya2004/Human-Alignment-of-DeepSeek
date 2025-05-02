import json

with open('./dataset/english_TQ_scores.json','r') as f:
    english_scores = json.load(f)

with open('./dataset/telugu_TQ_scores.json','r') as f:
    telugu_scores = json.load(f)

with open('./dataset/hindi_TQ_scores.json','r') as f:
    hindi_scores = json.load(f)

with open('./dataset/oriya_TQ_scores.json','r') as f:
    oriya_scores = json.load(f)

english_scores_truth =  0 
english_scores_align = 0

telugu_scores_truth = 0
telugu_scores_align = 0

hindi_scores_truth = 0
hindi_scores_align = 0

oriya_scores_truth = 0
oriya_scores_align = 0

for i in range(len(english_scores)):
    english_scores_truth += english_scores[i]['Truthfulness']
    english_scores_align += english_scores[i]['Alignment']

for i in range(len(telugu_scores)):
    telugu_scores_truth += telugu_scores[i]['Truthfulness']
    telugu_scores_align += telugu_scores[i]['Alignment']

for i in range(len(hindi_scores)):
    hindi_scores_truth += hindi_scores[i]['Truthfulness']
    hindi_scores_align += hindi_scores[i]['Alignment']

for i in range(len(oriya_scores)):
    oriya_scores_truth += oriya_scores[i]['Truthfulness']
    oriya_scores_align += oriya_scores[i]['Alignment']

english_scores_truth = english_scores_truth / len(english_scores)
english_scores_align = english_scores_align / len(english_scores)

telugu_scores_truth = telugu_scores_truth / len(telugu_scores)
telugu_scores_align = telugu_scores_align / len(telugu_scores)

hindi_scores_truth = hindi_scores_truth / len(hindi_scores)
hindi_scores_align = hindi_scores_align / len(hindi_scores)

oriya_scores_truth = oriya_scores_truth / len(oriya_scores)
oriya_scores_align = oriya_scores_align / len(oriya_scores)

print("English scores truth: ", english_scores_truth)
print("English scores align: ", english_scores_align)

print("Telugu scores truth: ", telugu_scores_truth)
print("Telugu scores align: ", telugu_scores_align)

print("Hindi scores truth: ", hindi_scores_truth)
print("Hindi scores align: ", hindi_scores_align)

print("Oriya scores truth: ", oriya_scores_truth)
print("Oriya scores align: ", oriya_scores_align)
