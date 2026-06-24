import numpy as np
from scipy.stats import norm

S = 256.75
K = 255
r = 0.0541
sigma = 0.3253
T = 22/365

d1 = (np.log(S/K) + (r + sigma**2/2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

call = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
put = K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

print(f"d1: {d1:.4f}")
print(f"d2: {d2:.4f}")
print(f"N(d1): {norm.cdf(d1):.4f}")
print(f"N(d2): {norm.cdf(d2):.4f}")
print(f"BS Call Price: {call:.2f}")
print(f"BS Put Price: {put:.2f}")