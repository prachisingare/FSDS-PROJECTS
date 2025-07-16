# 📊 Seaborn Bootcamp Data Visualization App using Streamlit

Welcome to the **Seaborn Bootcamp** project! This is an interactive data visualization app built using **Streamlit** and **Seaborn**, allowing users to explore insights from the classic **`tips` dataset** using various types of plots.

---

## 📌 Project Overview

This project was developed as part of a data science bootcamp. The goal is to learn and demonstrate:

- How to use Seaborn for rich statistical visualizations
- How to build interactive visualization dashboards using Streamlit
- How to explore a dataset visually and draw insights

The `tips` dataset is used here, which is pre-loaded in Seaborn. It contains details about restaurant bills, tips, customer demographics, and dining time.

---

## 📚 Dataset Information

The dataset used is Seaborn's inbuilt **`tips`** dataset. It contains 244 rows and 7 columns.

| Column Name | Description                       |
|-------------|-----------------------------------|
| `total_bill`| Total bill (USD)                  |
| `tip`       | Tip given by customer             |
| `sex`       | Gender of the customer            |
| `smoker`    | Whether the customer is a smoker  |
| `day`       | Day of the week                   |
| `time`      | Lunch or Dinner                   |
| `size`      | Number of people in the group     |

---

## 📈 Visualizations Included

The Streamlit app lets users explore the dataset through the following **12+ plots**:

| 🔍 Plot Type       | 📋 Description                                                  |
|--------------------|----------------------------------------------------------------|
| Scatter Plot        | Visualizes `total_bill` vs `tip` by time and party size        |
| Line Plot           | Total bill by party size grouped by gender                     |
| Bar Plot            | Total bill across different days segmented by gender           |
| Box Plot            | Tip distribution by day and smoker status                      |
| Violin Plot         | Distribution of total bill by day and time                     |
| Count Plot          | Frequency count of entries by day and smoker                   |
| Regression Plot     | Regression line for tip vs total bill                          |
| Histogram           | Distribution of total bills with KDE overlay                   |
| Strip Plot          | Tip values over days                                           |
| KDE Plot            | Density plot of total bills segmented by gender                |
| Pair Plot           | Pairwise relationships between numeric variables               |
| Joint Plot          | Scatter with histograms for total bill and tip                 |
| Facet Grid          | Multi-plot layout by smoker and time using histogram           |

---

## 🛠️ Tech Stack

- **Python 3.7+**
- **Seaborn**
- **Pandas**
- **Matplotlib**
- **Streamlit**

---

