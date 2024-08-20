from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import json
import pandas as pd

# Define your desired weights (example: higher weight for bi-grams)
weights = (0.25, 0.25, 0.25, 0.25)  # Weights for uni-gram, bi-gram, tri-gram, and 4-gram
n_words = 10 # Filter out sentences with less than n words
type_of_data =  "input_output" # text column name in the json file

# Define file paths
candidate_file_path = 'A.json'
reference_file_path = 'B.json'
# Load candidate text from json file
with open(candidate_file_path, 'r') as f:
    candidate_data = json.load(f)

candidate_text = [item[type_of_data] for item in candidate_data if type_of_data in item]

# Load reference text from json file
with open(reference_file_path, 'r') as f:
    reference_data = json.load(f)

reference_text = [item[type_of_data] for item in reference_data if type_of_data in item]

# Ensure the files have the same number of lines
assert len(candidate_text) == len(reference_text)

# Create a smoothing function
smoothie = SmoothingFunction().method4 

# Calculate and print the BLEU score for each pair of lines
results = []
for i, (ref, cand) in enumerate(zip(reference_text, candidate_text)):
    ref_words = ref.split()
    cand_words = cand.split()
    if len(ref_words) > n_words and len(cand_words) > n_words:  # Check if both sentences have more than 10 words
        score = sentence_bleu(references= ref_words, 
                              hypothesis= cand_words, 
                              weights=weights,
                              smoothing_function= smoothie)
        results.append((i, score))  # Add the item number as the first column

# Save result into dataframe
df = pd.DataFrame(results, columns=["item", "score"])
# Save df to csv
df.to_csv('BLEU_A_vs_B.csv', index=False)