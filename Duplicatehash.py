import os
import hashlib

def compute_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        # Read file in chunks to handle large files
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

def list_files_with_hashes(directory_path):
    file_hash_map = {}

    print(f"\n🔍 Scanning directory: {directory_path}\n")

    for root, _, files in os.walk(directory_path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                hash_value = compute_sha256(full_path)
                print(f"{file} -> {hash_value}")
                
                if hash_value in file_hash_map:
                    file_hash_map[hash_value].append(full_path)
                else:
                    file_hash_map[hash_value] = [full_path]
            except Exception as e:
                print(f"Error reading file {full_path}: {e}")

    return file_hash_map

def show_duplicates(file_hash_map):
    print("\n🧾 Duplicate Files Found:")
    duplicates_found = False
    for hash_value, files in file_hash_map.items():
        if len(files) > 1:
            duplicates_found = True
            print(f"\nHash: {hash_value}")
            for f in files:
                print(f" - {f}")
    if not duplicates_found:
        print("No duplicate files found.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python sha256_file_check.py <directory_path>")
    else:
        dir_path = sys.argv[1]
        if os.path.isdir(dir_path):
            file_hashes = list_files_with_hashes(dir_path)
            show_duplicates(file_hashes)
        else:
            print("❌ Invalid directory path.")
# 🚀 How to run:
# 1. Save this file as: sha256_file_check.py
# 2. Open terminal/command prompt
# 3. Run: python sha256_file_check.py /path/to/your/folder
