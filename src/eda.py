import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from collections import Counter

DATA_PATH = Path("data/processed/transactions.csv")
OUT_DIR = Path("results")

def main():
    df = pd.read_csv(DATA_PATH)

    # Convert "items" (comma-separated string) into list of items
    transactions = df["items"].fillna("").apply(
        lambda x: [i.strip() for i in x.split(",") if i.strip()]
    )

    # Basket sizes
    basket_sizes = transactions.apply(len)

    # Item frequencies
    all_items = [item for basket in transactions for item in basket]
    freq = Counter(all_items)

    OUT_DIR.mkdir(exist_ok=True)

    # Plot 1: Top 15 most frequent items
    top_items = freq.most_common(15)
    items, counts = zip(*top_items)

    plt.figure()
    plt.bar(items, counts)
    plt.xticks(rotation=75, ha="right")
    plt.title("Top 15 Item Frequencies")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "item_frequencies.png")
    plt.close()

    # Plot 2: Basket size distribution
    plt.figure()
    plt.hist(basket_sizes, bins=30)
    plt.title("Basket Size Distribution")
    plt.xlabel("Items per transaction")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "basket_size_distribution.png")
    plt.close()

    # Print summary stats (for progress.md)
    print("EDA Summary")
    print("Transactions:", len(df))
    print("Unique items:", len(freq))
    print("Average basket size:", round(basket_sizes.mean(), 2))
    print("Median basket size:", basket_sizes.median())
    print("Saved plots to:", OUT_DIR)

if __name__ == "__main__":
    main()
