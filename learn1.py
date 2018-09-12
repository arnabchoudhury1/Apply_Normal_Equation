import pandas as pd
print("1")
import numpy as np
print("2")
# from numpy import genfromtxt
from numpy.linalg import inv
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("data.csv", header=None, usecols = [0, 0])
X = df.values
X = np.insert(X, 0, 1, axis=1)

df = pd.read_csv("data.csv", header=None, usecols = [1, 1])
Y = df.values

#X = np.ones((59, 1))

print("X = ")
print(X)
print(X.shape)
input("Enter to continue")

print("Y = ")
print(Y)
print(Y.shape)
input("Enter to continue")

X_trans = np.transpose(X)
print("X_trans =")
print(X_trans)
print(X_trans.shape)
input("Enter to continue")
A = inv(np.dot(X_trans, X))
print("A = ")
print(A)
print(A.shape)
input("Enter to continue")
B = np.dot(X_trans, Y)
print("B = ")
print(B)
print(B.shape)
input("Enter to continue")

theta = np.dot(A, B)

print(theta)

df = pd.read_csv("data.csv")
data = df.values.T.tolist()

y1 = int(theta[0])+int(theta[1])*0
y2 = int(theta[0])+int(theta[1])*550

plt.plot([0, 550], [y1, y2], 'k-', data[0], data[1], 'ro')
plt.ylabel('Brain Weight')
plt.xlabel('Body Weight')

plt.show()

