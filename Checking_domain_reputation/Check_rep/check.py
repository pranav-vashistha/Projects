import os
import threading

def search_in_file(filename, search_string, results):
    found_entries = []
    with open(filename, 'r') as file:
        entries = file.readlines()
        found_entries = [entry.strip() for entry in entries if search_string in entry]
    results[filename] = found_entries

def search_in_files(files, search_string):
    results = {}
    threads = []

    for file in files:
        thread = threading.Thread(target=search_in_file, args=(file, search_string, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

if __name__ == "__main__":
    files = ['D:\\Jupyter notebooks\\Check_rep\\list1.txt', 'D:\\Jupyter notebooks\\Check_rep\\list3.txt', 'D:\\Jupyter notebooks\\Check_rep\\list4.txt', 'D:\\Jupyter notebooks\\Check_rep\\list5.txt', 'D:\\Jupyter notebooks\\Check_rep\\list7.txt', 'D:\\Jupyter notebooks\\Check_rep\\list8.txt', 'D:\\Jupyter notebooks\\Check_rep\\list12.txt', 'D:\\Jupyter notebooks\\Check_rep\\list16.txt']
    search_string = input("Enter the search domain")

    results = search_in_files(files, search_string)
    for filename, found_entries in results.items():
        print(f"Found in {filename}: {len(found_entries)} entries")
