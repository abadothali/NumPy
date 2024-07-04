import numpy as np

# Arrays........
# Zero daimancial array.....
zeroNd=np.array(787)
print(zeroNd)
print(zeroNd.ndim,"daimancial array......")
print()

# one dainecioal array......
oneNd=np.array([1,2,3,4,5])
print(oneNd)
print(oneNd.ndim,"daimancial array......")
print()

# two dainencial array.............
twoNd=np.array([[1,2,3,4,5],[7,8,9,4,3]])
print(twoNd)
print(twoNd.ndim,"dianencial array............")

# Arrays Operations..........
# check size...............
print("\nArrays size.....")
print(zeroNd.size)
print(oneNd.size)
print(twoNd.size)

# check memory size......
print("\nmemory size.....")
print(zeroNd.nbytes)
print(oneNd.nbytes)
print(twoNd.nbytes)

# check single items size in memory.........
print("\nSingle items size.....")
print(zeroNd.itemsize)
print(oneNd.itemsize)
print(twoNd.itemsize)

# check arrays datatypes...........
print("\nArrays datatypes...")
print(zeroNd.dtype)
print(oneNd.dtype)
print(twoNd.dtype)

# example a string datatype.....
str=np.array([['monirul'],['rupsa']])
print("\nExample in string........")
print(str.ndim,"dainciel arrays..........")
print(str)
print(str.size)
print(str.dtype)