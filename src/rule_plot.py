import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

RULES_PATH = Path("results/rules.csv")
OUT_PATH = Path("results/rules_scatter.png")

def main():
    rules = pd.read_csv(RULES_PATH)

    plt.figure()
    plt.scatter(rules["support"], rules["confidence"])
    plt.xlabel("Support")
    plt.ylabel("Confidence")
    plt.title("Association Rules: Support vs Confidence")
    plt.tight_layout()
    plt.savefig(OUT_PATH)
    plt.close()

    print("Saved:", OUT_PATH)

if __name__ == "__main__":
    main()
