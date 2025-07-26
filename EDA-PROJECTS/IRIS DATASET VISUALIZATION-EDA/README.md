# 🌸 Iris Dataset Visualization - EDA with Seaborn and Matplotlib

This project showcases **Exploratory Data Analysis (EDA)** and **Data Visualization** of the famous Iris dataset using Python libraries such as **Seaborn**, **Matplotlib**, and **Pandas**. The goal is to understand the patterns, distributions, and relationships among the features and species in the dataset.

---

## 📂 Project Overview

This analysis includes:
- Dataset loading and preprocessing
- Descriptive statistics
- Univariate, bivariate, and multivariate visualizations
- Interactive-style plots using Seaborn’s advanced features
- Dashboard-like layout of plots for comparative analysis

---


## 📌 Dataset Overview

The Iris dataset is a classic dataset used for classification and clustering tasks. It contains **150 records** with the following **5 columns**:

| Column           | Description                          |
|------------------|--------------------------------------|
| `SepalLengthCm`  | Sepal length in centimeters          |
| `SepalWidthCm`   | Sepal width in centimeters           |
| `PetalLengthCm`  | Petal length in centimeters          |
| `PetalWidthCm`   | Petal width in centimeters           |
| `Species`        | Iris flower species (Setosa, Versicolor, Virginica) |

Each species has 50 samples in the dataset.

---

## 🧰 Technologies Used

- Python 🐍
- Pandas
- Seaborn
- Matplotlib
- Jupyter Notebook

---

## 🔍 EDA and Visualization Summary

### 1. 📦 Data Preparation
- Loaded the dataset using `pd.read_csv()`
- Removed the `Id` column
- Checked null values, data types, and basic statistics

### 2. 📊 Univariate Analysis
- Bar plots to show class distribution of `Species`
- Histograms and distplots to visualize feature distributions
- KDE plots for density estimation

### 3. 📈 Bivariate and Multivariate Analysis
- **JointPlots** (scatter, regression, hex) for two-variable relationships
- **BoxPlots**, **StripPlots**, and **ViolinPlots** to compare feature distributions across species
- **SwarmPlots** for clustered scatter visualizations
- **FacetGrids** to split data visualization by category
- **PairPlots** for feature-pair comparison with class hue
- **Heatmap** for feature correlation analysis

### 4. 📐 Custom Dashboards and Layouts
- Combined multiple plots into a subplot-style dashboard (2x2 layout)
- Used color, size, and aesthetics to enhance visual storytelling

### 5. 📚 Additional Plots
- **Boxen plots** for fine-grained distribution view
- **LM plots** (Linear Model) to see regression lines between features
- **Area plots** for cumulative feature visualizations
- **Stacked Histograms** grouped by species

---

## 📌 Sample Visuals

Here are some of the plots included in this project:

- 🟩 Countplot of Species Distribution  
- 📉 Scatter plot of Sepal vs Petal features  
- 📦 Boxplot with overlayed StripPlot  
- 🔥 Heatmap of feature correlations  
- 🌈 Pairplot grouped by species  
- 🧠 KDE Density Plots for specific species  
- 📊 Dashboard layout (4 plots in one view)

---

# 📌 Insights
Petal features (Length & Width) show strong correlation and clearly separate the species.

Sepal features show more overlap between Versicolor and Virginica.

Iris-setosa is linearly separable and most distinct visually.

All three species have exactly 50 samples each.

prediction

# 👩‍💻 Author
- Prachi Singare
- 🎓 B.Tech in Artificial Intelligence and Data Science (2025)
- 🔍 Passionate about data analytics and machine learning

📫 LinkedIn

💻 GitHub




