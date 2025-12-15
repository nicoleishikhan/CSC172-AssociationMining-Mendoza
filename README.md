# Association Rule Mining of Student Purchase Patterns in Campus Convenience Stores

**CSC172 Data Mining and Analysis – Initial Project Plan**  
*Mindanao State University – Iligan Institute of Technology*  

**Student:** Nicole Ishi Khan P. Mendoza, 2021-1427
**Semester:** AY 2025–2026 Sem 1  

---

## 1. Project Overview
This project applies **association rule mining using the Apriori algorithm** to analyze student purchase patterns in campus convenience stores. The goal is to identify frequently co-purchased items and generate meaningful association rules that can support product placement, bundling, and inventory decisions in small retail environments such as university canteens and convenience stores.

---

## 2. Project Plan
The project will be completed in the following stages:

1. Dataset acquisition and understanding  
2. Data preprocessing and transaction basket creation  
3. Exploratory data analysis (EDA)  
4. Association rule mining using the Apriori algorithm  
5. Rule evaluation using support, confidence, lift, and conviction  
6. Visualization of results and interpretation  
7. Documentation and video presentation  

---

## 3. Dataset Choice
An **existing, publicly available transactional dataset** will be used to avoid surveys or manual data collection.

- **Dataset:** Online Retail II Dataset  
- **Source:** UCI Machine Learning Repository / Kaggle  
- **Domain:** Retail transaction data  
- **Description:** Contains invoice-level purchase records including product descriptions and quantities  
- **Accessibility:** Publicly available and downloadable online  
- **Planned Storage:** `data/online_retail_ii.csv`

This dataset is suitable for association rule mining because it contains real-world transaction data that can be converted into market basket format.

---

## 4. Planned Architecture / Workflow
```
Raw Transaction Data
↓
Data Cleaning & Preprocessing
↓
Transaction Basket Construction
↓
One-Hot Encoding
↓
Exploratory Data Analysis
↓
Apriori Algorithm
↓
Association Rule Generation
↓
Evaluation & Interpretation
```

