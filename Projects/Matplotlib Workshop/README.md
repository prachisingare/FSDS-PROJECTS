# 📊 Matplotlib Data Visualization Workshop

A hands-on data visualization project using **Matplotlib**, **Pandas**, and an interactive UI powered by **Gradio**.

---

## 🧾 Project Description

This project visualizes **Sales** and **Profit** data for six months using various charts. It also includes an interactive Gradio web app that allows users to choose the type of plot dynamically.

---

## 📊 Dataset

The dataset is created manually using Python dictionaries and converted into a Pandas DataFrame:

```
data = {
    "Month": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    "Sales": [10000, 12000, 15000, 13000, 17000, 16000],
    "Profit": [2000, 3000, 4000, 5000, 2500, 2000]
}
```
 ## 📈 Visualizations
We demonstrate multiple plot types:

📉 Line Plot – Sales trends over months

📊 Bar Plot – Comparison of Sales and Profit

🥧 Pie Chart – Profit share per month

✨ Scatter Plot – Sales vs Profit

## 📉 Histogram – Sales distribution

📦 Box Plot – Profit distribution

Each visualization is created using matplotlib.pyplot.

## 🖥️ Interactive Dashboard (Gradio)
An interactive web-based interface allows users to select any plot type and visualize it instantly. Built with Gradio, it includes:

Radio button interface to select plot type

Automatic rendering of the selected chart

