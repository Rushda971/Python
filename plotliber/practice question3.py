#scatter
import numpy as np
import matplotlib.pyplot as plt
x=np.array([2,4,6,8,10,12,14,16,18])
y=np.array([68,75,82,88,94,96,99,97,95])
#plt.scatter(x,y,color="blue")
plt.hist(x,y,color="blue")
plt.title("fitness tracker")
plt.xlabel=("hourse studied")
plt.ylabel=("exam score")
plt.show()
