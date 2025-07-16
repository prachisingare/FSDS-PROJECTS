.

🎬 IMDB Movie Rating Analysis using Pandas
📁 1. Dataset Overview
Three key datasets were used:

movies.csv: Contains movieId, title, and genres for ~27,000 movies.

ratings.csv: Contains 20 million+ user ratings (userId, movieId, rating, timestamp).

tags.csv: ~465,000 user-generated tags for various movies.

🔧 2. Data Preprocessing & Cleaning
Missing Values:

movies and ratings had no missing data.

tags had some missing rows, which were successfully dropped.

Columns Removed:

timestamp column from ratings and tags was dropped since it wasn't required for the analysis.

Data Types:

Ensured compatibility of numerical operations (e.g., rating as float).

📊 3. Descriptive Statistics on Ratings
plaintext
Copy code
count      ≈ 20 million
mean       ≈ 3.53
std dev    ≈ 1.05
min        = 0.5
max        = 5.0
mode       = 4.0
Most ratings were between 3.0 and 4.5.

A histogram and boxplot confirmed the skewed but central distribution.

🔎 4. Tags Analysis
Total tags (after cleaning): 465,548

Most common tags:

"in Netflix queue", "atmospheric", "superhero", "funny", etc.

Least common tags were specific and often appeared only once (e.g., "killer fish", "Paul Adelstein").

Bar charts visualized tag popularity.

🎥 5. Genre-Based Filtering
Action Movies were filtered using:

python
Copy code
is_action = movies['genres'].str.contains('Action')
Example Action Films:

GoldenEye, Heat, Assassins, Mortal Kombat, From Dusk Till Dawn

🧮 6. Statistical Insights from Ratings
Ratings Count per Rating Value:
Rating	Count
0.5	239,125
1.0	680,732
3.0	4,291,193
4.0	5,561,926 ← Most common
5.0	2,898,660

Ratings per Movie:
Highly rated movies (many had consistent 5.0 ratings).

Aggregated average ratings for each movieId.

📌 7. Data Filtering Examples
Extracted highly-rated movies:

python
Copy code
ratings[ratings['rating'] == 5.0]
Filtered based on genre and tag presence.

🔗 8. Merging Datasets
Merged movies with tags using:

python
Copy code
merged_df = movies.merge(tags, on='movieId', how='inner')
This allowed for analyzing:

Which tags are associated with highly rated or specific genre movies.

Movie descriptions enriched with user sentiments.

Example:

Toy Story (1995) → tagged with “Pixar animation”, “Disney”, “computer animation”

📉 9. Correlation Analysis
python
Copy code
ratings.corr()
userId	movieId	rating
userId	1.000	-0.0008	0.0012
movieId		1.000	0.0026
rating			1.000

Low correlation among columns—indicating rating is not strongly dependent on userId or movieId alone.

📌 Key Findings
Most ratings are between 3.0–4.0, indicating users tend to rate favorably.

4.0 is the most common rating.

Action and Comedy are dominant genres.

User-generated tags provide rich insight into movie themes (dark hero, noir thriller, etc.).

Highly rated films show consistent patterns in both ratings and user tags.

📈 Visualizations (Generated)
Histogram of ratings

Boxplot of ratings

Bar chart of most frequent tags


