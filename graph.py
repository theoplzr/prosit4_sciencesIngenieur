import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file containing test results
df = pd.read_csv("resultats_tests.csv")

# Keep only the rows where a HashMap result exists (i.e. a valid pair was found)
df = df[df["Résultat HashMap"].notnull()]

if df.empty:
    print("No result with a valid pair found. Charts will not be generated.")
else:
    # Retrieve the target value from the first row
    target = df["Target"].iloc[0]

    # Extract relevant columns
    fichiers = df["Fichier"]
    brute_times = df["Brute Force (s)"]
    hashmap_times = df["HashMap (s)"]
    x = np.arange(len(fichiers))  # X-axis positions for bars

    # === Chart 1: Brute Force Execution Time ===
    plt.figure(figsize=(12, 6))
    min_height = 0.002  # Minimum visual height to make very small bars visible

    # Draw bars manually with forced visible height, and display true values
    for i in range(len(brute_times)):
        real_height = brute_times.iloc[i]
        visible_height = max(real_height, min_height)
        plt.bar(x[i], visible_height, color='steelblue')
        plt.text(x[i], visible_height, f'{real_height:.6f}',
                 ha='center', va='bottom', fontsize=8)

    plt.title(f"Execution Time - Brute Force (Target = {target})")
    plt.xlabel("Data File")
    plt.ylabel("Time (seconds)")
    plt.xticks(x, fichiers, rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    filename1 = f"graph_brute_force_target_{target}.png"
    plt.savefig(filename1)
    print(f"Brute Force chart saved: {filename1}")

    # === Chart 2: HashMap Execution Time ===
    plt.figure(figsize=(12, 6))
    bars2 = plt.bar(x, hashmap_times, color='orange')

    # Display execution time on top of each bar
    for i, bar in enumerate(bars2):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.6f}',
                 ha='center', va='bottom', fontsize=8)

    plt.title(f"Execution Time - HashMap (Target = {target})")
    plt.xlabel("Data File")
    plt.ylabel("Time (seconds)")
    plt.xticks(x, fichiers, rotation=45)

    # Disable scientific notation on the Y-axis
    plt.ticklabel_format(style='plain', axis='y')

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    filename2 = f"graph_hashmap_target_{target}.png"
    plt.savefig(filename2)
    print(f"HashMap chart saved: {filename2}")

    plt.show()
