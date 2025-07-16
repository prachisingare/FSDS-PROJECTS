# 📊 Matplotlib Data Visualization Workshop

A hands-on data visualization project using **Matplotlib**, **Pandas**, and an interactive UI powered by **Gradio**.

---

## 🧾 Project Description

This project visualizes **Sales** and **Profit** data for six months using various charts. It also includes an interactive Gradio web app that allows users to choose the type of plot dynamically.

---

## 📊 Dataset

The dataset is created manually using Python dictionaries and converted into a Pandas DataFrame:

```python
data = {
    "Month": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    "Sales": [10000, 12000, 15000, 13000, 17000, 16000],
    "Profit": [2000, 3000, 4000, 5000, 2500, 2000]
}

