# 📈 Automated Equity Valuation Engine (DCF)

## 📌 Project Overview
As a Mechanical Engineering student at IIT Madras, I am trained to model physical systems to predict future performance. I built this tool to apply those same systems-modeling principles to the financial markets. This engine automates the **Discounted Cash Flow (DCF)** analysis, allowing for a data-driven approach to determining the intrinsic value of a company.

## ⚙️ How It Works
The engine follows a rigorous quantitative process to value a stock:
* **Real-Time Data Extraction:** Integrates with the `yfinance` API to pull the latest Free Cash Flow (FCF), total debt, and cash reserves directly from financial statements.
* **Projections:** Models a 5-year growth trajectory based on historical performance and terminal value.
* **Discounting Logic:** Applies the **Time Value of Money** principle by discounting future cash flows back to the present using a 10% WACC (Weighted Average Cost of Capital).
* **Margin of Safety:** Compares the calculated "Intrinsic Value" against the current "Market Price" to identify undervalued opportunities.

## 🛠 Technical Features
* **Financial Automation:** Replaced manual spreadsheet entry with a Python-based automation layer.
* **API Integration:** Leverages the `yfinance` library for seamless data sourcing.
* **Algorithmic Modeling:** Uses mathematical loops to calculate cumulative present value and terminal growth.
* **Systematic Analysis:** Built with modular functions to allow for easy adjustment of WACC and growth rate assumptions.


