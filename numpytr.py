#Q1
import numpy as np
randomnum= np.random.rand(10,1)
print(randomnum)
npmean=np.mean(randomnum)
print("Mean of elements is: ",npmean)

#Q2
randomnum = np.random.rand(20,1)
print(randomnum)
print("standard deviation is: ",np.std(randomnum))
print("variance is: ",np.var(randomnum))

#Q3
randomnum1= np.random.rand(10,20)
randomnum2= np.random.rand(20,25)
npsum = np.dot(randomnum1,randomnum2)
print("Matrix Multiplication is \n",npsum)
print("sum of elememts in multiplication array is: ", np.sum(npsum))

A = np.arange(1,11).reshape(10,1)
def function(x):
    return 1 / (1 + np.exp(-x))

function = np.vectorize(function)
array = function(A) 
print("after applyin function to A: \n",array)
