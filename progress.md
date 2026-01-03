# CSC172 Association Rule Mining Project – Progress Report

**Student:** Nicole Ishi Khan P. Mendoza, 2021-1427  
**Repository:** https://github.com/nicoleishikhan/CSC172-AssociationMining-Mendoza  

---

## 📊 Current Status

| Milestone | Status | Notes |
|---------|--------|------|
| Dataset Preparation | ✅ Completed | Online Retail II dataset loaded |
| Data Preprocessing | ✅ Completed | Cleaned invoices, grouped transactions |
| EDA | ⏳ In Progress | Item frequencies and basket size analysis |
| Apriori Implementation | ⏳ In Progress | Frequent itemsets generated |
| Rule Evaluation | ⏳ Pending | Support, confidence, lift computation |

---

## 1. Dataset Progress
- **Source:** Online Retail II Dataset (UCI / Kaggle)
- **Total transactions:** ~500,000 raw rows
- **Processed baskets:** ~25,000 transactions
- **Unique items:** ~4,000 (filtered to frequent items)

---

## 2. Preprocessing Summary
- Removed cancelled invoices
- Filtered negative quantities
- Grouped items by InvoiceNo
- Converted to transaction baskets
- One-hot encoded transactions

---

## 3. EDA Progress
- Top frequent items identified
- Average basket size computed
- Initial visualizations generated

---

## 4. Next Steps
- Run Apriori with tuned thresholds
- Generate top 25 association rules
- Export results to CSV
- Add visualizations to README
