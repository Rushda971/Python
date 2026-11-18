import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Sample OHLC data: [Open, High, Low, Close]
np.random.seed(0)
days = 10
price = np.random.uniform(100, 110, size=(days, 4))  # Open, High, Low, Close

# Sort OHLC for logical consistency
price[:, 1] = np.maximum(price[:, 0], price[:, 1])  # High >= Open
price[:, 2] = np.minimum(price[:, 0], price[:, 2])  # Low <= Open
price[:, 3] = price[:, 3]  # Close (can be anywhere between high and low)

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))

width = 0.6
for i, (o, h, l, c) in enumerate(price):
    color = 'green' if c > o else 'red'
    
    # Wick
    ax.plot([i, i], [l, h], color='black', linewidth=1)
    
    # Body
    rect = Rectangle((i - width/2, min(o, c)), width, abs(c - o),
                     color=color, alpha=0.8)
    ax.add_patch(rect)

ax.set_xlim(-1, days)
ax.set_title('Candlestick Chart (Using NumPy + Matplotlib)')
ax.set_xlabel('Day')
ax.set_ylabel('Price')
plt.grid(True)
plt.show()
