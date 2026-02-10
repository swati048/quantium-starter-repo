# 📊 Soul Foods Pink Morsel Sales Visualizer

Interactive data visualization dashboard built with **Python Dash** to explore regional sales trends and answer a business question:

> Were sales higher before or after the Pink Morsel price increase on Jan 15, 2021?

---

## Preview
![Dashboard](assets/dashboard.png)

---

## 🚀 Features

* Data cleaning & transformation with **Pandas**
* Interactive line chart using **Plotly**
* Region filtering via radio buttons
* Styled responsive UI
* Automated UI testing with **Pytest + Dash Testing**

---

## 🛠 Tech Stack

* Python 3.9
* Dash
* Plotly
* Pandas
* Pytest
* Selenium (Dash testing)

---

## 📈 Running the App

### Clone repo

```bash
git clone https://github.com/swati048/quantium-starter-repo.git
cd quantium-starter-repo
```

### Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run dashboard

```bash
python app.py
```

Visit:

```
http://127.0.0.1:8050
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🐛 Troubleshooting

### "selenium.common.exceptions.WebDriverException"
```bash
# This command finds the driver path and adds it to your current session
$env:PATH += ";$(python -c 'from webdriver_manager.chrome import ChromeDriverManager; print(ChromeDriverManager().install())' | Split-Path)"
```

---

## 📊 Business Insight

From the visualization, sales trends before and after the price change can be compared interactively by region, enabling data-driven decision making.

---

## 👩‍💻 Author

Swati Thakur
