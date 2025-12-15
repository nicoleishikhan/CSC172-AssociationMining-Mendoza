# CSC172 Association Rule Mining Project Proposal  
**Student:** Nicole Ishi Khan P. Mendoza, 2021-1427  
**Date:** December 12, 2025  

## 1. Project Title  
Association Rule Mining of Student Purchase Patterns in Campus Convenience Stores


## 2. Problem Statement
Campus convenience stores serve students who make frequent, small-item purchases such as snacks, beverages, and basic school supplies. Despite the availability of transactional purchase records, these data are often underutilized when making decisions related to product placement, bundling, and inventory management.

This project analyzes retail transaction data to identify frequent itemsets and strong association rules that represent common co-purchase patterns. The insights derived from this analysis may support data-driven decision-making for small-scale retail environments similar to campus convenience stores.


## 3. Objectives
- Preprocess transactional data and perform exploratory data analysis (EDA) with visualizations  
- Implement the Apriori algorithm to generate association rules  
- Evaluate rules using support, confidence, lift, and conviction metrics  


## 4. Dataset Plan
- **Source:** Online Retail II Dataset – UCI Machine Learning Repository  
  https://archive.ics.uci.edu/ml/datasets/Online+Retail+II  
- **Domain:** Retail transaction data  
- **Description:** Contains invoice-level transaction records including product descriptions and quantities  
- **Estimated size:** ~500,000 transaction records  
- **Acquisition:** Direct download from UCI Repository → saved as `data/online_retail_ii.csv`  


## 5. Technical Approach
- **Preprocessing:**  
  - Remove cancelled transactions and missing values  
  - Group items by transaction (invoice)  
  - Convert transactions into one-hot encoded format using `TransactionEncoder`  
- **Algorithm:**  
  - Apriori algorithm (min_support = 0.02, min_confidence = 0.6, min_lift = 1.2)  
- **Framework:**  
  - Python, pandas, mlxtend, matplotlib, seaborn  
- **Environment:**  
  - Jupyter Notebook / VS Code  


## 6. Expected Challenges & Mitigations
- **Challenge:** Sparse transaction matrix  
  - **Solution:** Filter infrequent items using minimum support threshold  

- **Challenge:** Large dataset size leading to long runtime  
  - **Solution:** Limit maximum itemset length and reduce dataset scope  

- **Challenge:** Generation of trivial or uninformative rules  
  - **Solution:** Apply lift threshold (> 1.2) and confidence filtering  
