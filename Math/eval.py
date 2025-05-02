import json
import os
RESULTS_FOLDER = "./results/"
result_files = os.listdir(RESULTS_FOLDER)
for result_file in result_files:
    with open(os.path.join(RESULTS_FOLDER, result_file), "r") as f:
        results = json.load(f)

    accuracy = 0
    for result in results:
        org_ans = str(result["Original Answer"])
        if "cot" in result_file: gen_ans = result["Response"].strip().split("\n")[-1].replace(',', '').strip()
        elif "std" in result_file: gen_ans = result["Response"].strip().split("\n")[0].replace(',', '').strip()
        else: raise Exception("Wrong file")
        
        accuracy += 1 if org_ans in gen_ans else 0

    print(f"{result_file}: ", accuracy/len(results))
