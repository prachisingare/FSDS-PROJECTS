# 📊 Exploratory Data Analysis (EDA) on Employee Dataset

This project performs **Exploratory Data Analysis (EDA)** on a raw employee dataset using Python libraries such as `pandas`, `numpy`, `seaborn`, and `matplotlib`. The goal is to clean, transform, visualize, and prepare the data for future machine learning tasks.

---

## 📖 What is EDA?

**Exploratory Data Analysis (EDA)** is a critical step in the data science process. It involves:

- Understanding the structure of the dataset
- Detecting missing or incorrect values
- Identifying patterns, anomalies, and relationships
- Visualizing the data for deeper insights

---

## 🔧 EDA Techniques Used

- **Data Cleaning**  
  Removed special characters using regular expressions and standardized formats

- **Missing Value Treatment**  
  - Filled `Age` and `Exp` using **mean**
  - Filled missing `Location` using **mode**

- **Data Transformation**  
  - Converted columns to correct data types (e.g., `int`, `category`)
  - Extracted numeric values from text using regex

- **Feature Engineering**  
  Created one-hot encoded variables using `pd.get_dummies()`

- **Data Visualization**  
  - Distribution plots for Salary
  - Histograms for Experience
  - Regression plots (`lmplot`) to analyze relationship between `Exp` and `Salary`

---

## 📦 Dataset Features

The dataset contains the following columns:

| Column   | Description              |
|----------|--------------------------|
| Name     | Employee name            |
| Domain   | Area of work             |
| Age      | Age of the employee      |
| Location | Work location            |
| Salary   | Monthly salary (₹)       |
| Exp      | Years of experience      |

---

## 📁 Output Files

- ✅ Cleaned CSV: `clean_data.csv`
- 📈 Visual plots: Salary & Experience distribution, linear regression

---

## 📚 Libraries Required

- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`

---



