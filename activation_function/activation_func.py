import numpy as np
import matplotlib.pyplot as plt
x = np.array([0.5, 1.0])
w = np.array([0.2, 0.8])
b = 0.1
y=np.dot(x, w) + b
def linear(x):
    return x
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def relu(x):    
    return np.maximum(0, x)
def tanh(x):
    return np.tanh(x)
s=sigmoid(y)  
r=relu(y)
t=tanh(y)
l=linear(y)
sdev=s*(1-s)
rdev=np.where(r > 0, 1, 0)
tdev=1 - t**2  
ldev=1
plt.plot(y, s, label='Sigmoid', color='blue', marker='o')
plt.plot(y, sdev, label="Sigmoid Derivative", color='blue', marker='x')
plt.plot(y, r, label='relu', color='red', marker='o')
plt.plot(y, rdev, label="relu Derivative", color='red', marker='x')
plt.plot(y, t, label='tanh', color='green', marker='o')
plt.plot(y, tdev, label="tanh Derivative", color='green', marker='x')
plt.show()
plt.plot(y, l, label='linear', color='black', marker='o')
plt.plot(y, ldev, label="linear Derivative", color='black', marker='x')
plt.show()