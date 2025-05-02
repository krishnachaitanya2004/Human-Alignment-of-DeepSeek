# CS6103 Final Project: Evaluating Alignment of DeepSeek Model

This project evaluates the DeepSeek model across six diverse datasets to analyze its alignment with human values—truthfulness, respectfulness, helpfulness, and bias mitigation.

---

## Evaluation Instructions

Go to the respective folder and follow the instructions

### Truthfulness Evaluation

Run the following for each language:

- `python3 generate.py [lang]`
- After generating for all languages: `python3 eval.py`

---

### Translation Evaluation

Evaluate translations using IN22 and Mann Ki Baat datasets:

- `python3 generate_IN22.py [lang]`
- `python3 generate_mann_ki_baat.py [lang]`
- Then run: `python3 eval.py`

---

### Toxicity Evaluation

To assess toxic content in model responses:

- `python3 generate.py`
- `python3 eval.py`

---

### Socio-Cultural Bias Evaluation

Supported categories: `Age`, `Gender_identity`, `Religion`

- `python3 generate.py --category [Age | Gender_identity | Religion]`
- `python3 eval.py --category [Age | Gender_identity | Religion]`

---

### Math Reasoning (Across Cultural Groups)

Evaluate reasoning using identity-sensitive prompts:

- `python3 generate.py [type] [prompt]`
- `python3 eval.py`

Where `[type]` ∈ { `indian`, `muslim`, `north_east`, `hindu`, `east`, `western`, `south` }  
And `[prompt]` ∈ { `std`, `cot` }

---

### Cultural Understanding

Run the following:

- `python3 generate.py`

---

Results are stored automatically and can be used to compare across tasks and models. Ensure all generation steps are completed before running `eval.py`.

