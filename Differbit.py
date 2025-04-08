import os
import hashlib
from itertools import combinations

def sha256_hash(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    return hashlib.sha256(content).digest()

def bit_difference(hash1, hash2):
    xor_result = bytes(a ^ b for a, b in zip(hash1, hash2))
    return sum(bin(byte).count('1') for byte in xor_result)

def compare_file_hashes(directory):
    file_hashes = {}

    # Step 1: Hash all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            path = os.path.join(directory, filename)
            file_hashes[filename] = sha256_hash(path)

    # Step 2: Compare all pairs
    diff_counts = {1: 0, 2: 0, 3: 0}
    for (file1, hash1), (file2, hash2) in combinations(file_hashes.items(), 2):
        diff = bit_difference(hash1, hash2)
        if diff in diff_counts:
            diff_counts[diff] += 1
        print(f"{file1} vs {file2}: {diff} bits different")

    return diff_counts

# Example usage
directory_path = "your_directory_here"  # replace with your folder path
result = compare_file_hashes(directory_path)
print("\nSummary:")
print("1-bit differences:", result[1])
print("2-bit differences:", result[2])
print("3-bit differences:", result[3])
