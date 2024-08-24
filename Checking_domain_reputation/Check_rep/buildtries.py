from pytrie import StringTrie
import os

def build_tries_from_files(file_paths):
    tries = {}
    for file_path in file_paths:
        trie = StringTrie()
        with open(file_path, 'r') as file:
            for line in file:
                domain = line.strip()
                trie[domain] = True
        tries[file_path] = trie
    return tries

def save_tries(tries, save_directory):
    os.makedirs(save_directory, exist_ok=True)
    for file_path, trie in tries.items():
        file_name = os.path.basename(file_path)
        save_path = os.path.join(save_directory, f"{file_name}.txt")
        with open(save_path, 'w') as file:
            for key in trie.keys():
                file.write(key + '\n')

def load_trie(load_path):
    trie = StringTrie()
    with open(load_path, 'r') as file:
        for line in file:
            domain = line.strip()
            trie[domain] = True
    return trie

# Example usage:
input_files = [f"D:\\Jupyter notebooks\\Check_rep\\list{i}.txt" for i in range(1, 18)]  # List of input file paths f"D:\\Jupyter notebooks\\Check_rep\\list{i}.txt" for i in range(1, 18)
output_directory = 'D:\\Jupyter notebooks\\Check_rep\\blacklist trie'

# Build tries from files
tries = build_tries_from_files(input_files)

# Save tries to files
save_tries(tries, output_directory)

# Example usage of loaded tries
for file_path, trie in tries.items():
    print(f"Trie for {file_path}:")
    for key in trie.keys(prefix='example'):
        print(key)


