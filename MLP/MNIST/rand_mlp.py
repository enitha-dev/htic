import numpy as np
np.random.seed(100)
in_size=784
h1_size=64
h2_size=32
out_size=10

def xav_weights(size):
    return np.random.randn(*size) * np.sqrt(2.0 / size[0])

w1=xav_weights((in_size, h1_size))
b1 = np.zeros(h1_size)
w2 = xav_weights((h1_size, h2_size))
b2 = np.zeros(h2_size)
w3 = xav_weights((h2_size, out_size))
b3 = np.zeros(out_size)

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    exps=np.exp(x - np.max(x))
    return exps / np.sum(exps, axis=1, keepdims=True)

x= np.random.randn(1, in_size)  
target = np.array([[3]])


def cross_en(pred,target):
    return -np.log(pred[0, target[0,0]])


lr=0.01
epoch=100
losses = []

for e in range(epoch): 
    tot_loss=0
    correct = 0
    for i in range(100):
        x = np.random.randn(1, in_size) 
        target = np.array([[np.random.randint(0, out_size)]])

        z1 = x @ w1 + b1
        a1 = relu(z1)   
        z2 = a1 @ w2 + b2
        a2 = relu(z2)
        z3 = a2 @ w3 + b3
        a3 = softmax(z3)

        if np.argmax(a3) == target[0, 0]:
            correct += 1
        #print("Predicted class:", np.argmax(a3), "Actual class:", target[0, 0])

        loss = cross_en(a3, target)

        dz3 = a3.copy()
        dz3[0, target[0, 0]] -= 1

        dw3 = a2.T @ dz3
        db3 = dz3

        da2 = dz3 @ w3.T
        dz2 = da2 * (z2 > 0).astype(float)

        dw2 = a1.T @ dz2
        db2 = dz2

        da1 = dz2 @ w2.T
        dz1 = da1 * (z1 > 0).astype(float)

        dw1 = x.T @ dz1
        db1 = dz1

        w3 -= lr * dw3
        b3 -= lr * db3[0]
        w2 -= lr * dw2
        b2 -= lr * db2[0]
        w1 -= lr * dw1
        b1 -= lr * db1[0]

        tot_loss += loss
        avg_loss = np.mean(loss)
        losses.append(avg_loss)

    print(f"Epoch {e+1}, Accuracy: {correct / 10:.2f}, Total Loss: {tot_loss:.4f}")
  

    