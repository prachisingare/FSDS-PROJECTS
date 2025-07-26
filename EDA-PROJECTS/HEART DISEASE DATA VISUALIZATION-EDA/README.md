# 📊 Heart Disease Analysis - Exploratory Data Analysis (EDA)
This project presents an in-depth exploratory data analysis (EDA) of a heart disease dataset using Python. The analysis includes univariate, bivariate, and multivariate visualizations to uncover patterns and correlations among the variables and the presence of heart disease.

---

## 📊 Dataset Information

The dataset contains **303 observations** with **14 features**. The `target` column indicates the presence or absence of heart disease.

| Feature      | Description |
|--------------|-------------|
| `age`        | Age of the patient |
| `sex`        | Sex (1 = male, 0 = female) |
| `cp`         | Chest pain type (0–3) |
| `trestbps`   | Resting blood pressure (mm Hg) |
| `chol`       | Serum cholesterol (mg/dl) |
| `fbs`        | Fasting blood sugar > 120 mg/dl (1 = true; 0 = false) |
| `restecg`    | Resting electrocardiographic results (0–2) |
| `thalach`    | Maximum heart rate achieved |
| `exang`      | Exercise-induced angina (1 = yes; 0 = no) |
| `oldpeak`    | ST depression induced by exercise |
| `slope`      | Slope of the peak exercise ST segment |
| `ca`         | Number of major vessels colored by fluoroscopy |
| `thal`       | Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect) |
| `target`     | Target (1 = heart disease, 0 = no heart disease) |

---

## 🔧 Technologies Used

- **Python**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Scipy**

---

## ✅ EDA Process Breakdown

### 1. 📥 Data Loading and Inspection
- Imported dataset using `pandas`
- Checked data shape, column names, and types
- Verified absence of missing values
- Ensured no negative or invalid data values

### 2. 🧮 Statistical Summary
- Used `.describe()` to understand range, mean, quartiles, etc.
- Verified basic statistics for each variable

### 3. 📈 Univariate Analysis
- Plotted **countplots**, **histograms**, and **KDE** plots for:
  - `age`, `sex`, `cp`, `chol`, `thalach`, `fbs`, etc.
- Analyzed distribution of each variable individually

### 4. 🧑‍🤝‍🧑 Bivariate Analysis
- Analyzed correlation of features with `target`
- Plotted:
  - Countplots with `hue='target'`
  - Box plots and strip plots for `thalach`, `age`, etc.
  - Scatter plots for continuous variables

### 5. 🔥 Multivariate Analysis
- Generated **heatmap** for correlation matrix
- Identified features with strong positive/negative correlation to heart disease
- Created **pairplots** for selected continuous variables

### 6. 🚨 Outlier Detection
- Used box plots for outlier detection on:
  - `age`, `trestbps`, `chol`, `thalach`, `oldpeak`
- Analyzed distributions to detect potential data anomalies

---

## 📉 Key Insights

- Patients with **higher chest pain types (`cp`)** and **maximum heart rate (`thalach`)** are more likely to have heart disease.
- Variables like `exang`, `oldpeak`, and `ca` showed **negative correlation** with heart disease.
- Strong positive correlations:
  - `cp`, `thalach`, `slope`
- Strong negative correlations:
  - `oldpeak`, `exang`, `ca`, `thal`, `sex`

---
.

# 📊 Visualizations Included
Count plots of target, cp, sex, fbs, exang

KDE and Histogram plots of continuous variables

Strip and box plots for visualizing distributions across target

Correlation heatmap

Pair plots

---

# ✅ Conclusion
This EDA provides comprehensive insights into factors affecting heart disease. It highlights important correlations (e.g., high chest pain type or max heart rate with heart disease presence) and prepares the dataset for machine learning or statistical modeling.


---


# 🙋‍♀️ About the Author
- Prachi Singare
- B.Tech in Artificial Intelligence and Data Science (2025)
- Passionate about data analysis, machine learning, and creating insights from data.

🔗 [LinkedIn](www.linkedin.com/in/prachi-singare13)

💻 [GitHub](https://github.com/prachisingare)


