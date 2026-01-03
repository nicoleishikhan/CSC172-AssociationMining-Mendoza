import pandas as pd
from pathlib import Path
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

DATA_PATH = Path("data/processed/transactions.csv")
OUT_DIR = Path("results")

MIN_SUPPORT = 0.02
MIN_CONFIDENCE = 0.60
MIN_LIFT = 1.20

def main():
    df = pd.read_csv(DATA_PATH)

    # Convert comma-separated items into list
    transactions = df["items"].fillna("").apply(
        lambda x: [i.strip() for i in x.split(",") if i.strip()]
    ).tolist()

    # One-hot encoding
    te = TransactionEncoder()
    te_array = te.fit(transactions).transform(transactions)
    onehot = pd.DataFrame(te_array, columns=te.columns_)

    # Apriori frequent itemsets
    frequent_itemsets = apriori(
        onehot,
        min_support=MIN_SUPPORT,
        use_colnames=True
    )

    # Generate association rules
    rules = association_rules(
        frequent_itemsets,
        metric="confidence",
        min_threshold=MIN_CONFIDENCE
    )

    # Filter by lift
    rules = rules[rules["lift"] >= MIN_LIFT]

    OUT_DIR.mkdir(exist_ok=True)

    # Save outputs
    frequent_itemsets.to_csv(OUT_DIR / "frequent_itemsets.csv", index=False)
    rules.to_csv(OUT_DIR / "rules.csv", index=False)

    # Top 25 rules by lift and confidence
    top25 = rules.sort_values(
        ["lift", "confidence"],
        ascending=False
    ).head(25)

    top25.to_csv(OUT_DIR / "rules_top25.csv", index=False)

    print("Apriori completed")
    print("Frequent itemsets:", len(frequent_itemsets))
    print("Rules after filtering:", len(rules))
    print("Saved:")
    print("- results/frequent_itemsets.csv")
    print("- results/rules.csv")
    print("- results/rules_top25.csv")

if __name__ == "__main__":
    main()
