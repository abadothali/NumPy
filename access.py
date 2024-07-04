import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])

# Accesing Elements.........
# Acces specifix elements........
print(arr[0,0])   # Output => 1
print(arr[1,2])   # Output => 8

# Accsing specific rows........
print(arr[0,:])

# Slicing: Elements => Starting to Ending point....
# note: last element in slicing not includee.......
arr2=np.array([10,11,12,13,14,15,16,17,18,19,20])
print("\nSlicing.......")
print(arr2[2:7])

# Slicing when we not no ending point..........
print("\nSlicing when we not no ending point..........")
print(arr2[5:])

# Slicing when we not no starting point..........
print("\nSlicing when we not no starting point..........")
print(arr2[:11])

# Slicing in two dainencial arrays.......
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("\nSlicing in two dainencial arrays.......")
print(arr[1,2:5]) # Output=> [8 9 10]

# Copy Arrays.........
x=arr.copy()
print("\nCopy Arrays..........")
print(x)