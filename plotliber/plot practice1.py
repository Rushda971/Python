import matplotlib.pyplot as plt
import numpy as np
#normal
"""xpoint=np.array([1,2,3,4,5,6,7,8,9,10])
ypoint=np.array([2,4,6,8,10,12,14,16,18,20])
plt.plot(xpoint,ypoint)"""
#sales data
products =np.array(['Laptops', 'Phones', 'Tablets', 'Monitors', 'Keyboards'])
sales =np.array([300, 500, 250, 200, 150])
plt.plot(products,sales)
plt.title("Product Sales Overview")

plt.xlabel("product names")
plt.ylabel("no.of sales")
#pie chart
plt.show()
