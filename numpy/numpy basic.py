#file ko module ke name se save maat karo
#numpy(data ko change karna easy hai)
#basic program
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
#through indexing
print(arr[0])
#through dimension(indexing + printing)
#0 dimension
arr=np.array(42)
print("0 dimension:",arr)
#1 dimension
arr=np.array([1,2,3,4,5,6])
print("1 dimension:",arr)
print("indexing 1D:",arr[5])#indexing
arr[4]=99
print(arr)
#tuple in array
arr=np.array((1,2,3,4,5))
print("tuple to list:",arr)
#2 dimension
print("2 D dimensional")
arr=np.array([[1,2,3,4]])
arr1=np.array([[1,2,3],[3,4,4]])
print("check",arr.ndim)
print(arr)
print(type(arr))
print(arr.ndim)
#3 dimension
print("3 D dimensional")
arr=np.array([[[1,2,3,4]]])
arr1=np.array([[[1,2,3],[3,4,4]]])
print("check:",arr1.ndim)
arr2=np.array([[1,2,3],[14,5,6],[7,8,9]])
print("check2:",arr2.ndim)
print(arr)
print(type(arr))
print(arr.ndim)
#version
print(np.__version__)
#slicing
arr=np.array([58,78,54,34,98,76,54])
print(arr[2:6:1])
print(arr[4:])
#base:return the data(owns the data)
#copy owns the data
#copy(changes make in array are not affected)
#copy return none 
x=arr.copy()
arr[0]=0
print(arr)
print(x)
#view (changes make in are affected in array)
#view return original value
#view does not owns data
x=arr.copy()
y=arr.view()
print(x.base)
print(y.base)
#sum(indexing)
arr=np.array([1,2,3,4,5,6])
x=arr[2]+arr[4]
print("sum:",x)
#printing using string and indexing
arr2=np.array([[1,2,3],[14,5,6],[7,8,9]])
print(arr2[2,0:2])
#slicing
print("slice:",arr2[0:3,2:4])
#datatype
#astype:allow copy of array and allow user to specify datatype in parameter





