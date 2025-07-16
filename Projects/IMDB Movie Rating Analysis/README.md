# 🎬 IMDB Movie Rating Analysis using Pandas

This project performs exploratory data analysis (EDA) on IMDB movie data using Python and the Pandas library. It includes data cleaning, statistical analysis, visualization, and merging datasets to gain insights about movie ratings, genres, and user preferences.

---

## 📁 Dataset Overview

Three datasets used:
- `movies.csv`: Movie titles and genres (~27K rows)
- `ratings.csv`: 20M+ user ratings with timestamps
- `tags.csv`: 465K+ user-generated tags

---

## 🔧 Data Preprocessing

- Dropped unnecessary `timestamp` columns.
- Checked for and handled missing values:
  - `tags.csv` had missing values, which were removed.
- Ensured correct data types for analysis.

---

## 📊 Descriptive Statistics

- Ratings range: 0.5 to 5.0
- Most frequent rating: 4.0
- Mean rating: 3.52
- Used histogram and boxplot for visualization

---

## 🔎 Tags Analysis

- Cleaned tag data to remove nulls
- Top tags: "in Netflix queue", "superhero", "funny", "dark hero"
- Used bar charts to visualize top tags

---

## 🎥 Genre-Based Filtering

Filtered genres using string operations, e.g., movies tagged with 'Action':
```python
is_action = movies['genres'].str.contains('Action')
```

---

## 📈 Group By and Aggregation

- Counted number of ratings per rating score
- Calculated average rating per movie
- Identified most and least rated movies

---

## 🔗 Merging Datasets

Merged `movies` and `tags`:
```python
merged_df = movies.merge(tags, on='movieId', how='inner')
```

This helped analyze which tags are used for top-rated or specific-genre movies.

---

## 📌 Key Findings

- Ratings mostly lie between 3.0 and 4.5
- Action and Comedy are the most common genres
- 4.0 is the most common rating
- Some movies consistently receive 5.0 ratings
- Tags add valuable user sentiment

---


