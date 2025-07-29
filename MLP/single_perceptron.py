import numpy as np
x = np.array([19, 0])
w = np.array([1.2, 0.6])
out=0
lr=0.5
thres=1

def acti(z):
    if z >= thres:
        return 1
    else:
        return 0

z = np.dot(x, w)
output = acti(z)
print("output:", output)
print("w:", w)
while True:
    if output !=out:
        w = w + lr * (out - z) * x
        print("changing w to:", w)
        z= np.dot(x, w)
        output = acti(z)
        print("curr z:", z)
        print("curr output:", output)
    else:
        print("final weights:", w)
        print("final output:", output)
        break