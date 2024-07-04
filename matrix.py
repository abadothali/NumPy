import numpy as np

# Zero matrix........
a=np.zeros((4,6))  # zeros((Row,Column))
print(a)

# One matrix.........
x=np.ones((6,4,5))
print(x)    # ones(total matrix,Row,Column)

# full matrix.........
y=np.full((7,3),786)    # full((Rows,Column),Matrix Number)
print(y)

# identity matrix..........
z=np.identity(7)
print("\nidentity matrix..........")
print(z)