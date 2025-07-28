
# 📊 LLM-Powered Exploratory Data Analysis (EDA)

This project is a web-based application that performs **automated Exploratory Data Analysis (EDA)** on any dataset using **Python**, **Gradio**, **Pandas**, **Matplotlib**, **Seaborn**, and **Ollama's Mistral-7B** model.

Just upload your CSV file, and get a complete EDA report including:
- Missing value handling
- Summary statistics
- AI-generated insights using LLM
- Interactive visualizations (histograms, heatmaps)

---
.

## 🔍 Features
📁 Upload any CSV dataset

📈 Auto-generated statistical summary

🧠 AI-generated insights using Mistral-7B via Ollama

📊 Data visualizations (histograms, heatmaps)

🧼 Handles missing values automatically

⚡ Interactive and user-friendly Gradio interface

🌐 Option to share the app via a public link

---

## 🛠️ Tech Stack

| Component            | Description                         |
| -------------------- | ----------------------------------- |
| Python               | Main programming language           |
| Gradio               | Web interface for model interaction |
| Pandas               | Data manipulation and analysis      |
| Matplotlib & Seaborn | Data visualizations                 |
| Ollama (Mistral)     | AI-powered text insights            |


---
### 🚀 How It Works
Upload CSV File via the Gradio interface.

Missing Values Handling:

Numeric columns → Filled with median

Categorical columns → Filled with mode (currently incorrectly uses median, to be fixed)

Summary Statistics are generated using pandas.describe().

AI Insights:

Summary passed to Mistral-7B via Ollama

Returns text-based insights

Data Visualizations:

Histograms for each numeric column

Correlation heatmap for all numeric features

Output:

Text report (summary + AI insights)

Gallery of visualizations

---
## 👨‍💻 Author
Prachi Singare
B.Tech in Artificial Intelligence and Data Science, 2025
LinkedIn: linkedin.com/in/prachi-singare
