# MACD & 200-day EMA Trading Strategy

## Overview

This project implements a trading strategy based on the MACD indicator and the 200-day Exponential Moving Average (EMA) to analyze stock performance. The script fetches historical stock data, calculates key technical indicators, generates buy and sell signals, and evaluates the performance of the trading strategy.

## Features

- **Historical Data Fetching**: Retrieve stock data from Yahoo Finance.
- **MACD Calculation**: Compute the MACD and Signal Line to identify buy/sell signals.
- **200-day EMA Calculation**: Compute the 200-day EMA to filter trading signals.
- **Signal Generation**: Identify buy and sell signals based on MACD crossovers and EMA positioning.
- **Performance Metrics**: Calculate target gains and stop loss losses.
- **Visualization**: Plot stock prices, the 200-day EMA, and trading signals.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages:
  - `yfinance`
  - `pandas`
  - `numpy`
  - `matplotlib`

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Run the script:**

    ```bash
    python trading_strategy.py
    ```

2. **Outputs:**
    - Buy and sell signals with corresponding dates.
    - Target gains and stop loss losses in percentage.
    - Net percentage gain from the strategy.
    - A CSV file (`BHEL_NSE_MACD_EMA_Strategy.csv`) with detailed data.
    - A plot (`trading_strategy_plot.png`) for visual analysis.

## Results

The strategy was tested on `BANKBARODA.NS` from `2021-01-01` to `2024-01-01`. Key performance metrics include:
- **Target Hits**: Number of times the target was achieved.
- **Stop Loss Hits**: Number of times the stop loss was triggered.
- **Net Percentage Gain**: Overall gain after accounting for stop losses.
