from scipy.stats import norm
import numpy as np

S = 256.75
K = 255
r = 0.0541
sigma = 0.3253
T = 22/365

d1 = (np.log(S/K) + (r + sigma**2/2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

delta = norm.cdf(d1)
gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
vega = S * norm.pdf(d1) * np.sqrt(T) / 100  # per 1% move in vol
theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) - r * K * np.exp(-r*T) * norm.cdf(d2)) / 365

print(f"Delta: {delta:.4f}")
print(f"Gamma: {gamma:.6f}")
print(f"Vega: {vega:.4f}")
print(f"Theta: {theta:.4f}")