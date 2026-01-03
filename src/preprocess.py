import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/online_retail_II.xlsx")   # change to .csv if needed
OUT_PATH = Path("data/processed/transactions.csv")

def load_raw(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".xlsx":
        return pd.read_excel(path)
    return pd.read_csv(path, encoding="latin1")

def main():
    df = load_raw(RAW_PATH)
    
    print("COLUMNS:", list(df.columns))
    print(df.head(3))


    # Keep only needed columns (ignore if some names differ slightly)
    # Normalize column names (strip spaces)
    df.columns = [c.strip() for c in df.columns]

    # Try common invoice column name variants
    invoice_candidates = ["InvoiceNo", "Invoice", "Invoice No", "invoice", "invoice_no", "invoiceNo"]
    desc_candidates = ["Description", "Item", "Product", "product", "description"]
    qty_candidates = ["Quantity", "Qty", "quantity", "qty"]

    def pick_col(candidates):
        for c in candidates:
            if c in df.columns:
                return c
        return None

    invoice_col = pick_col(invoice_candidates)
    desc_col = pick_col(desc_candidates)
    qty_col = pick_col(qty_candidates)

    if not invoice_col or not desc_col or not qty_col:
        raise KeyError(
            f"Missing required columns. Found columns: {list(df.columns)}\n"
            f"Need invoice/description/quantity, got: invoice={invoice_col}, desc={desc_col}, qty={qty_col}"
        )

    df = df[[invoice_col, desc_col, qty_col]].copy()
    df.columns = ["InvoiceNo", "Description", "Quantity"]  # rename to standard names


    # Drop missing
    df = df.dropna(subset=["InvoiceNo", "Description"])

    # Remove cancelled invoices like 'C536365'
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)
    df = df[~df["InvoiceNo"].str.startswith("C")]

    # Keep positive quantities
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df = df[df["Quantity"] > 0]

    # Normalize item names
    df["Description"] = (
        df["Description"].astype(str).str.lower().str.strip()
    )

    # Group into baskets
    baskets = (
        df.groupby("InvoiceNo")["Description"]
        .apply(lambda x: sorted(set(x)))  # unique items per invoice
        .reset_index()
        .rename(columns={"Description": "items"})
    )

    # Save as CSV (items stored as comma-separated)
    baskets["items"] = baskets["items"].apply(lambda lst: ", ".join(lst))

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    baskets.to_csv(OUT_PATH, index=False)

    print("Saved:", OUT_PATH)
    print("Transactions:", len(baskets))
    print("Example row:\n", baskets.head(1))

if __name__ == "__main__":
    main()
