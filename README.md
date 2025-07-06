
<div align="center">
  <h1>📊 Python Data Stats Analyzer</h1>
</div>

<p align="center">
  <em>A Python script for performing descriptive statistical analysis, visualizing data with boxplots, and removing outliers.</em>
</p>

---

## 📌 Overview

**Data Stats Analyzer** is a Python-based tool designed to analyze numerical datasets.  
It reads data from a CSV file, calculates key statistical measures such as mean, median, mode, and more.  
It also detects and removes outliers using the IQR method and visualizes the cleaned data using boxplots.

---

## 📈 What It Calculates

- Arithmetic Mean
- Median
- Mode
- Range
- Mean Absolute Deviation (MAD)
- Variance
- Standard Deviation
- Coefficient of Variation
- Interquartile Range (IQR)

All results are written to a `sonuc.txt` file.

---

## 📦 Project Structure

```
data-stats-analyzer/
│
├── veri_seti.csv      # Input CSV file (your dataset)
├── sonuc.txt          # Output file with calculated statistics
├── analyzer.py        # Main Python script
└── README.md          # Project documentation
```

---

## 📊 Visual Output

- Generates a **boxplot** for each column in the dataset using `matplotlib`.
- Helps visualize the spread of the data and potential outliers.

---

## 🧼 Outlier Detection

- Detects outliers for each column using the **Interquartile Range (IQR)** method.
- Removes detected outliers before performing statistical calculations.

---

## 🛠️ Requirements

- **Python 3.x**
- `pandas`
- `matplotlib`

To install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

1. Clone or download this repository.

2. Place your dataset in the root directory as `veri_seti.csv`.

3. Run the analyzer:

```bash
python analyzer.py
```

4. Check:
   - `sonuc.txt` for statistical results.
   - Boxplot windows for visual insights.

---

## 📄 License

This project is intended for educational and data analysis practice purposes.  
Feel free to fork, improve, and use in your own projects.

---

## 🙋‍♂️ Author

| Platform | Info |
|----------|------|
| 📧 Email | [batuhanisiklar0@gmail.com](mailto:batuhanisiklar0@gmail.com) |
| 💼 LinkedIn | [Batuhan Işıklar](https://www.linkedin.com/in/batuhanisiklar/) |

---

> Made with 📊 and 🧠 by Batuhan Işıklar
