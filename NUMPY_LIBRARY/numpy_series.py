import numpy as Mp
#1d Array......
# l=[1,2,3,4,5]
# arr1=Mp.array([1,2,3,4,5])
# print(type(l))
# print(type(arr1))
# print(arr1.ndim)
# print(arr1.shape)
#2d Array...../
# arr2=Mp.array([[[1,2,3],[4,5,6]]])
# print(arr2.shape)
# print(arr2.ndim)
#3d Array....
# arr3=Mp.array([[[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4]]])
# print(arr3.shape)
# print(arr3.ndim)/
#Array Creation....
#zero Matrix
# z0=Mp.zeros((5,2,2),dtype='int')
# print(z0)
#for Specific value
# full1=Mp.full((3,2),3)
# print(full1)
#identity matrix
identity=Mp.eye(5,dtype='int')
print(identity)

