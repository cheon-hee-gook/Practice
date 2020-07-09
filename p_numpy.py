import numpy as np

# arr1 = np.array([1,2,3])#list
# print(arr1)
# arr2 = np.array((2,4,6))#tuple
# print(arr2)
# arr3 = np.arange(0,10,2)
# arr4 = np.append(arr3,[1,2,3])
# print(arr4)

# arr5 = np.linspace(0,20, 4) #사분위수?
# print(arr5)

# arr6 = np.ones((2,3))
# print(arr6)

# arr7 = np.zeros((2,3))
# print(arr7)

# print(len(arr3))
# print(arr3.size)

# arr8 = np.array([[1,2,3],[4,5,6]])
# # print(arr8)
# arr9 = np.delete(arr8,1,axis = 1)
# print(arr9)


# arr = np.arange(10)
# arr1 = arr.reshape(2,5)
# print(arr1)


arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.repeat(arr1,3)
# print(arr1 + arr2)
# print(arr3)
print(np.cumsum(arr3))