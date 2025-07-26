# 🎬 Movie Rating Analysis – Exploratory Data Analysis (EDA)

This project is a comprehensive **Exploratory Data Analysis (EDA)** of a movie ratings dataset using Python’s **Pandas**, **Seaborn**, and **Matplotlib** libraries. The goal is to explore how variables like **Critic Ratings**, **Audience Ratings**, **Budgets**, **Genres**, and **Year of Release** interact and influence each other.

---

## 📦 Dataset Overview

The dataset used contains **559 movies** with the following features:

| Column Name        | Description                                        |
|--------------------|----------------------------------------------------|
| `Film`             | Title of the movie                                 |
| `Genre`            | Genre of the movie (e.g., Action, Drama, Comedy)   |
| `CriticRating`     | Rotten Tomatoes critic score (0-100)               |
| `AudienceRating`   | Rotten Tomatoes audience score (0-100)             |
| `BudgetMillions`   | Estimated budget of the movie in millions          |
| `Year`             | Year of release                                    |

All entries are non-null and clean. Some columns were converted to categorical data types to optimize memory and improve plotting efficiency.

---

## 📈 EDA Objectives

The main goals of this exploratory data analysis are:

- Understand the distribution of ratings and budgets.
- Compare **critic vs audience** reception.
- Explore how genres influence rating or budget.
- Visualize trends over **different years**.
- Create meaningful **multi-dimensional plots** (e.g. Genre vs Year vs Ratings).

---

## 🔧 Technologies Used

- **Python 3**
- **Pandas** – for data manipulation
- **Seaborn** – for high-level visualizations
- **Matplotlib** – for custom plots
- **Jupyter Notebook** – for running interactive EDA

---

## 🧪 Data Preparation

Key data preparation steps:
- Renamed columns for consistency.
- Converted columns to appropriate data types (`category`, `int64`).
- Verified no missing/null values.
- Ensured all numeric columns are within logical ranges.

---

## 📊 Univariate Visualizations

Explored single-variable distributions using:
- `sns.histplot()` and `plt.hist()` for **AudienceRating**, **CriticRating**, and **BudgetMillions**.
- `sns.displot()` with different bin sizes and KDEs.
- Distribution analysis by filtering genres such as `Drama`, `Action`, `Romance`, etc.

---

## 📈 Bivariate Visualizations

To compare two variables:
- `sns.jointplot()` for **AudienceRating vs CriticRating** with scatter and hexbin.
- `sns.kdeplot()` to visualize the **2D density estimate**.
- `sns.lmplot()` to group by genre and remove regression lines for clear clustering.
- `sns.boxplot()` and `sns.violinplot()` for **Genre vs Ratings** and **Year vs Ratings**.

---

## 📊 Multivariate Visualizations

To explore relationships across more than two dimensions:
- `FacetGrid` from Seaborn to create **grid plots** by `Genre` and `Year`.
- Scatter plots and histograms nested inside grids.
- 2x2 **Matplotlib subplot dashboards** combining:
  - Budget vs AudienceRating KDE
  - Budget vs CriticRating KDE
  - Year-wise rating distributions
  - Genre-focused violinplots

---

## 📌 Key Insights

- **Critic and audience ratings** are moderately correlated, but some genres (like Action) show larger disagreement.
- Budget is **not directly correlated** with higher ratings.
- **Dramas and thrillers** are more consistent in critic ratings; **comedies** show greater variance.
- Most movies in the dataset were released around **2008–2010**, forming the densest group.
- Visual styles like KDE and Violin plots help to uncover **hidden distributions** not visible through basic scatter plots.

---

# 🎬 Movie Rating Analysis – Exploratory Data Analysis (EDA)

This project is a comprehensive **Exploratory Data Analysis (EDA)** of a movie ratings dataset using Python’s **Pandas**, **Seaborn**, and **Matplotlib** libraries. The goal is to explore how variables like **Critic Ratings**, **Audience Ratings**, **Budgets**, **Genres**, and **Year of Release** interact and influence each other.

---

## 📦 Dataset Overview

The dataset used contains **559 movies** with the following features:

| Column Name        | Description                                        |
|--------------------|----------------------------------------------------|
| `Film`             | Title of the movie                                 |
| `Genre`            | Genre of the movie (e.g., Action, Drama, Comedy)   |
| `CriticRating`     | Rotten Tomatoes critic score (0-100)               |
| `AudienceRating`   | Rotten Tomatoes audience score (0-100)             |
| `BudgetMillions`   | Estimated budget of the movie in millions          |
| `Year`             | Year of release                                    |

All entries are non-null and clean. Some columns were converted to categorical data types to optimize memory and improve plotting efficiency.

---

## 📈 EDA Objectives

The main goals of this exploratory data analysis are:

- Understand the distribution of ratings and budgets.
- Compare **critic vs audience** reception.
- Explore how genres influence rating or budget.
- Visualize trends over **different years**.
- Create meaningful **multi-dimensional plots** (e.g. Genre vs Year vs Ratings).

---

## 🔧 Technologies Used

- **Python 3**
- **Pandas** – for data manipulation
- **Seaborn** – for high-level visualizations
- **Matplotlib** – for custom plots
- **Jupyter Notebook** – for running interactive EDA

---

## 🧪 Data Preparation

Key data preparation steps:
- Renamed columns for consistency.
- Converted columns to appropriate data types (`category`, `int64`).
- Verified no missing/null values.
- Ensured all numeric columns are within logical ranges.

---

## 📊 Univariate Visualizations

Explored single-variable distributions using:
- `sns.histplot()` and `plt.hist()` for **AudienceRating**, **CriticRating**, and **BudgetMillions**.
- `sns.displot()` with different bin sizes and KDEs.
- Distribution analysis by filtering genres such as `Drama`, `Action`, `Romance`, etc.

---

## 📈 Bivariate Visualizations

To compare two variables:
- `sns.jointplot()` for **AudienceRating vs CriticRating** with scatter and hexbin.
- `sns.kdeplot()` to visualize the **2D density estimate**.
- `sns.lmplot()` to group by genre and remove regression lines for clear clustering.
- `sns.boxplot()` and `sns.violinplot()` for **Genre vs Ratings** and **Year vs Ratings**.

---

## 📊 Multivariate Visualizations

To explore relationships across more than two dimensions:
- `FacetGrid` from Seaborn to create **grid plots** by `Genre` and `Year`.
- Scatter plots and histograms nested inside grids.
- 2x2 **Matplotlib subplot dashboards** combining:
  - Budget vs AudienceRating KDE
  - Budget vs CriticRating KDE
  - Year-wise rating distributions
  - Genre-focused violinplots

---

## 📌 Key Insights

- **Critic and audience ratings** are moderately correlated, but some genres (like Action) show larger disagreement.
- Budget is **not directly correlated** with higher ratings.
- **Dramas and thrillers** are more consistent in critic ratings; **comedies** show greater variance.
- Most movies in the dataset were released around **2008–2010**, forming the densest group.
- Visual styles like KDE and Violin plots help to uncover **hidden distributions** not visible through basic scatter plots.

---




