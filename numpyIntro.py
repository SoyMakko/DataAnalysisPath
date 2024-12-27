import numpy as np
import time 
import sys
import matplotlib.pyplot as plt

# Numpy is a Python library used for working with arrays, linear algebra, fourier transform and matrices.
# The array object here is called *ndarray*

# Creating an array
a = np.array([1,2,3,4,5])
print(a)
# You can access the elements tha same way 
print('a[0]\t ', a[0])
print(type(a)) #Type of the array
print(a.dtype) # Type of the data stored in the array

# Slicing in python means taking the elements from the given index to another given index.
# We pass slice like this: [start:end].The element at end index is not being included in the output.

b = a[0:3] # Selecting the elements from the 1st to the 2nd

print(b)

# We can also define the steps in slicing, like this: [start:end:step].

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

# If we don't pass start its considered 0
# If we don't pass end it considers till the length of array.
# If we don't pass step its considered 1

# Print the even elements in the given array.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1::2])

# Assign values with list

select = [0,2,3,4]
print(select)

# Use List to select elements

c = np.array([20, 1, 2, 3, 4])
d = c[select]
print(d)

c[select] = 100000
print(c)

# Get the size of numpy array

print("Size",a.size)

# Get the number of dimensions of numpy array.  The attribute ndim represents the number of array dimensions, or the rank of the array. In this case, one:

print("Dimension",a.ndim)

# Get the shape/size of numpy array. The attribute shape is a tuple of integers indicating the size of the array in each dimension:

print(" shape",a.shape)

### Numpy Statistical Functions

# Create a numpy array
a = np.array([1, -1, 1, -1])

# Get the mean of numpy array
mean = a.mean()
print("Mean",a)

# Unidimensional array
a = np.array([1, 2, 3, 4, 5])
mean = a.mean()  # mean = (1+2+3+4+5) / 5 = 3
print("Mean:", mean)  # Output: Mean: 3.0

# Multidimensional array
b = np.array([[1, 2, 3], [4, 5, 6]])
mean_all = b.mean()  # Media de todos los elementos: (1+2+3+4+5+6)/6 = 3.5
mean_axis0 = b.mean(axis=0)  # Media a lo largo de las columnas: [2.5, 3.5, 4.5]
mean_axis1 = b.mean(axis=1)  # Media a lo largo de las filas: [2.0, 5.0]

print("Mean all:", mean_all)  # Output: 3.5
print("Mean axis 0:", mean_axis0)  # Output: [2.5 3.5 4.

# Get the standard deviation of numpy array
standard_deviation=a.std()
standard_deviation

b = np.array([-1, 2, 3, 4, 5])
# Get the biggest value in the numpy array
max_b = b.max()
print(max_b)

# Get the smallest value in the numpy array
min_b = b.min()

## Numpy Array Operations

u = np.array([1,0])
v = np.array([0, 1])

z = np.add(u, v)

def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

# Plot numpy arrays

Plotvec1(u, z, v)
# plt.show()

# Substraction

a = np.array([10, 20, 30])
b = np.array([5, 10, 15])
c = np.subtract(a, b)
print(c)

# Array Multiplication

x = np.array([1, 2])
y = np.array([2, 1])

# Numpy Array Multiplication
z = np.multiply(x, y)

# Division
div = np.divide(x,y)
print(div)

# Dot product

X = np.array([1, 2])
print(X)
Y = np.array([3, 2])
a = np.dot(X, Y)
print(a)

## Adding a constant

# Create a constant to numpy array

u = np.array([1, 2, 3, -1]) 
b = u + 1
print(b)

# A useful function for plotting mathematical functions is linspace. Linspace returns evenly spaced numbers over a specified interval.
# numpy.linspace(start, stop, num = int value)
# start : start of interval range
# stop : end of interval range
# num : Number of samples to generate.

# Makeup a numpy array within [-2, 2] and 5 elements

print("Linespace",np.linspace(-2, 2, num=5))
print("Linespace with 9 elements",np.linspace(-2, 2, num=9))

# We can apply the sine function to each element in the array x and assign it to the array y:

y = np.sin(x)
plt.plot(x, y)
# plt.show()

a=np.array([-1,1]) 

b=np.array([1,1]) 

print(np.dot(a,b) )
X=np.array([[1,0,1],[2,2,2]]) 

out=X[0:2,2]
print(out)