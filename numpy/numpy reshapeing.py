#SHAPES
import numpy as np
arr=np.array([1,2,3,4],ndmin=5)
print(arr)
print(arr.shape)
print(arr.reshape(2,2))
print(arr.reshape(2,1,2))
#reshape(?)
#iteration
arr2=np.array([1,2,3,4,5])
for x in arr2:
    print(x)
    
#basic numpy
#create an array
arrays=np.array([1,3,4,5,6])
print("array:",arrays)

#array shapes and reshape
arr3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr3.reshape(3,4))

#data type
arr4=np.array([1,2,3,5.5])
print(arr4)
print(arr4.dtype)#yeh datatype baata hai
print(type(arr4))#yeh array type baata hai


#array of zeros and ones
#Create a 4x4 array of all zeros.
arr5=np.zeros((4,4))
print(arr5)
print(arr5.dtype)
#now why its returning float for 0 ?
#because bydefault np.zeros is float64
#if you want than you can define datatype as int
#now,question comes why its default zero because because float are more precise
#....and numpy application are in scientific calculation that why


#Create a 3x3 array filled with ones.
arr6=np.ones((3,3))
print(arr6)
print(arr6.dtype)

#but then again question comes then why for ones and empty
#To support floating point math out-of-the-box.
"""np.ones()	float64	Because 1.0 is more general than 1.
np.empty()	float64	Allows for decimal placeholders in future assignments."""

#Random values:
#Create a 2x3 array of random floats between 0 and 1 using NumPy.
import numpy as np
arr7 = np.random.rand(2, 3)  # 2 rows, 3 columns
print(arr7)
"""np.random.rand() is a NumPy function that generates random numbers following
a uniform distribution between 0 and 1. """


