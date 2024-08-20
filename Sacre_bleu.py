import json
import numpy as np
from datasets import load_metric as evaluate
import pandas as pd

# Variables
n_words = 10 # Filter out sentences with less than n words
type_of_data = "translated" # The column of candidate text in the json file
type_of_data_1 =  "original" # The column of reference text in the json file

# Define file paths
candidate_file_path = "A.json"
reference_file_path = 'B.json'
# Load candidate text from json file
with open(candidate_file_path, 'r') as f:
    candidate_data = json.load(f)

candidate_text = [item[type_of_data] for item in candidate_data if type_of_data in item]

# Load reference text from json file
with open(reference_file_path, 'r') as f:
    reference_data = json.load(f)

reference_text = [item[type_of_data_1] for item in reference_data if type_of_data_1 in item]

# Ensure the files have the same number of lines
assert len(candidate_text) == len(reference_text)

# Calculate and print the BLEU score for each pair of lines
metric_bleu = evaluate("sacrebleu")

# Loop through each pair of sentences and calculate the BLEU score
results = []
for i, (ref, cand) in enumerate(zip(reference_text, candidate_text)):
    ref_words = ref.split()
    cand_words = cand.split()
    if len(ref_words) > n_words and len(cand_words) > n_words:  # Check if both sentences have more than 10 words
        score = metric_bleu.compute(predictions=[cand_words], references=[ref_words])["score"]
        results.append((i, score))  # Add the item number as the first column

# Convert results to numpy array
bleu_results = np.array(results)

# Save result into dataframe
df = pd.DataFrame(bleu_results, columns=["item", "score"])
# Save df to csv
df.to_csv('BLEU_A_vs_B.csv', index=False)
