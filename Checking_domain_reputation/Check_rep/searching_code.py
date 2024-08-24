from pytrie import StringTrie
import os
import time
import re
from keras.models import model_from_json
from keras.preprocessing import sequence
import string

# Load top-1m trie
top_1m_trie = StringTrie()
with open("D:\\Jupyter notebooks\\Check_rep\\whitelist trie\\top-1m.txt.txt", 'r') as file:
    for line in file:
        domain = line.strip()
        top_1m_trie[domain] = True

# Load blacklist tries
blacklist_tries = {}
blacklist_directory = 'D:\\Jupyter notebooks\\Check_rep\\blacklist trie'
for file_name in os.listdir(blacklist_directory):
    if file_name.endswith('.txt'):
        file_path = os.path.join(blacklist_directory, file_name)
        trie = StringTrie()
        with open(file_path, 'r') as file:
            for line in file:
                domain = line.strip()
                trie[domain] = True
        blacklist_tries[file_name] = trie

# Function to extract domain from URL
def extract_domain(url):
    domain = re.search(r"https?://(www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,})/?", url)
    if domain:
        return domain.group(2)
    else:
        return None

# Preprocessing function
def preprocess_url(url):
    printable = string.printable
    # Convert raw URL string in list of lists
    url_int_tokens = [[printable.index(x) + 1 for x in url if x in printable]]
    # Cut URL string at max_len or pad with zeros if shorter
    max_len = 75
    X = sequence.pad_sequences(url_int_tokens, maxlen=max_len)
    return X

# Function to search query in tries
def search_query_in_tries(url):
    domain = extract_domain(url)
    if domain is None:
        print("Invalid URL")
        return

    # Search in top-1m trie
    if domain in top_1m_trie:
        print("Found in top-1m")
        return

    # Search in blacklist tries
    for file_name, trie in blacklist_tries.items():
        if domain in trie:
            print(f"Found in {file_name}")
            # Log the finding in blacklist.log
            with open("blacklist.log", "a") as log_file:
                log_file.write(f"Domain: {domain}, Trie: {file_name}, Time: {time.time()}\n")
            return

    # Load model
    model_name = "deeplearning_1DConv"
    model_path_json = "your_model_path_here.json"
    model_path_h5 = "your_model_path_here.h5"
    model = model_from_json(open(model_path_json).read())
    model.load_weights(model_path_h5)

    # Preprocess URL
    X = preprocess_url(url)
    # Pass preprocessed URL to machine learning model
    prediction = model.predict(X)
    if prediction == 1:
        # Log the result in model_block.log
        with open("model_block.log", "a") as log_file:
            log_file.write(f"URL: {url}, Time: {time.time()}\n")
    else:
        # Log the result in model_allow.log
        with open("model_allow.log", "a") as log_file:
            log_file.write(f"URL: {url}, Time: {time.time()}\n")

# Continuous search loop
while True:
    url = input("Enter URL (type 'quit' to exit): ")
    if url.lower() == 'quit':
        break
    search_start_time = time.time()
    search_query_in_tries(url)
    search_end_time = time.time()
    print(f"Search time: {search_end_time - search_start_time:.4f} seconds")
