import os
import pandas as pd
import time
from algos.force_brute import find_pair_brute_force
from algos.hash_map import find_pair_hash_map

# Load a CSV file and convert its first column to a list of integers
def load_data(path):
    df = pd.read_csv(path, skiprows=1, header=None)
    return df[0].astype(int).tolist()

# Run both algorithms and measure their execution time
def run_test(file_path, target):
    data = load_data(file_path)

    # Run brute force algorithm and measure time
    start = time.time()
    result1 = find_pair_brute_force(data, target)
    time_brute = time.time() - start

    # Run hash map algorithm and measure time
    start = time.time()
    result2 = find_pair_hash_map(data, target)
    time_hash = time.time() - start

    # Return a dictionary containing results
    return {
        "Fichier": os.path.basename(file_path),
        "Target": target,
        "Brute Force (s)": round(time_brute, 6),
        "Résultat Brute": result1,
        "HashMap (s)": round(time_hash, 6),
        "Résultat HashMap": result2
    }

if __name__ == "__main__":
    # You can change this target to test other values
    target = 134

    data_dir = "data"
    files = sorted(f for f in os.listdir(data_dir) if f.endswith(".csv"))

    all_results = []

    print(f"\n==========================")
    print(f"TEST FOR TARGET = {target}")
    print(f"==========================")

    # Run the test on each data file
    for file in files:
        path = os.path.join(data_dir, file)
        result = run_test(path, target)
        all_results.append(result)
        print(f"\nFile : {file} | Target : {target}")
        print(f"Brute Force : {result['Brute Force (s)']}s | Result : {result['Résultat Brute']}")
        print(f"HashMap : {result['HashMap (s)']}s | Result : {result['Résultat HashMap']}")

    # Save all results to a CSV file
    df = pd.DataFrame(all_results)
    df.to_csv("resultats_tests.csv", index=False)
    print("\nResults saved to 'resultats_tests.csv'")
