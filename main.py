import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


stock_data = yf.download('BANKBARODA.NS', start='2021-01-01', end='2024-01-01')


def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    data['EMA12'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['Signal_Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    return data


def calculate_ema(data, window=200):
    data['200EMA'] = data['Close'].ewm(span=window, adjust=False).mean()
    return data


def generate_signals(data):
    buy_signals = []
    sell_signals = []
    target_gains = []
    stop_loss_losses = []
    
    in_position = False
    entry_price = 0
    
    for i in range(1, len(data)):
        
        if (data['MACD'][i] > data['Signal_Line'][i]) and (data['MACD'][i-1] <= data['Signal_Line'][i-1]) and (data['Close'][i] > data['200EMA'][i]):
            if not in_position:
                buy_signals.append(data.index[i])
                entry_price = data['Close'][i]
                stop_loss = entry_price * 0.97
                target = entry_price * 1.03
                in_position = True
        
        
        if in_position:
            if data['Close'][i] <= stop_loss:
                sell_signals.append(data.index[i])
                stop_loss_loss = (stop_loss - entry_price) / entry_price * 100
                stop_loss_losses.append(stop_loss_loss)
                in_position = False
            elif data['Close'][i] >= target:
                sell_signals.append(data.index[i])
                target_gain = (data['Close'][i] - entry_price) / entry_price * 100
                target_gains.append(target_gain)
                in_position = False
    
    return buy_signals, sell_signals, target_gains, stop_loss_losses


stock_data = calculate_macd(stock_data)
stock_data = calculate_ema(stock_data)


buy_signals, sell_signals, target_gains, stop_loss_losses = generate_signals(stock_data)


total_target_gain = sum(target_gains)
total_stop_loss_loss = sum(stop_loss_losses)
net_percentage_gain = total_target_gain + total_stop_loss_loss


print("Buy Signals:")
for signal in buy_signals:
    print(signal)

print("\nSell Signals:")
for signal in sell_signals:
    print(signal)

print(f"\nTarget Hits: {len(target_gains)}")
print(f"Stop Loss Hits: {len(stop_loss_losses)}")


if target_gains:
    print("\nTarget Gains (%):")
    for gain in target_gains:
        print(f"{gain:.2f}%")
else:
    print("No target gains recorded.")

if stop_loss_losses:
    print("\nStop Loss Losses (%):")
    for loss in stop_loss_losses:
        print(f"{loss:.2f}%")
else:
    print("No stop loss losses recorded.")

print(f"\nNet Percentage Gain: {net_percentage_gain:.2f}%")


stock_data.to_csv('BHEL_NSE_MACD_EMA_Strategy.csv')


plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['200EMA'], label='200-day EMA', linestyle='--')
plt.scatter(buy_signals, stock_data.loc[buy_signals]['Close'], marker='^', color='g', label='Buy Signal', alpha=1)
plt.scatter(sell_signals, stock_data.loc[sell_signals]['Close'], marker='v', color='r', label='Sell Signal', alpha=1)
plt.title('BHEL.NS Buy and Sell Signals based on MACD and 200-day EMA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
