import pandas as pd
import numpy as np

df = pd.read_csv("eternal.csv", encoding='utf-8', encoding_errors='ignore')
df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

df['Log Return'] = np.log(df['Close Price'] / df['Close Price'].shift(1))

recent = df.tail(22)
sigma_daily = recent['Log Return'].std()
sigma_annual = sigma_daily * np.sqrt(252)

print(f"Daily Sigma: {sigma_daily:.6f}")
print(f"Annualised Sigma (Historical Vol): {sigma_annual:.4f}")