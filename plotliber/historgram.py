#histrogram
import matplotlib.pyplot as plt
import numpy as np
#x=np.random.normal(300,5,10)
"""Generate 1000 random numbers from a normal distribution with:
Mean = 50
Standard deviation = 8"""
x=np.random.normal(50,8,1000)
plt.hist(x,edgecolor="black",bins=40)
plt.show()
