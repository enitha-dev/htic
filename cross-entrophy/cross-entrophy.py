import numpy as np
true=np.array([1, 0, 1, 1, 0, 1, 0, 1, 0, 1])
pred=np.array([0.9, 0.1, 0.8, 0.7, 0.4, 0.9, 0.3, 0.8, 0.2, 0.95])
l=[]
for y, p in zip(true, pred):
    if y == 1:
        loss= -np.log(p)
    else:
        loss= -np.log(1-p)
    l.append(loss)
loss=np.array(l)
bce=np.mean(loss)
print("BCE:",bce)

from keras.losses import binary_crossentropy
bce_loss_keras = binary_crossentropy(true,pred).numpy()
print(f"Binary Cross-Entropy Loss (Keras): {bce_loss_keras}")

from keras.losses import categorical_crossentropy
true=np.array([[1,0,0],[0,1,0],[0,0,1],[1,0,0],[0,1,0]])
pred=np.array([[0.8,0.1,0.1],[0.2,0.7,0.1],[0.1,0.1,0.8],[0.85,0.1,0.05],[0.05,0.8,0.15]])
l=[]
for y, p in zip(true,pred):
    true_c=np.argmax(y)
    v= -np.log(p[true_c])
    l.append(v)
loss=np.array(l)
loss_cce=np.mean(loss)
print("loss cce:",loss)

categorical_bce_keras = categorical_crossentropy(true, pred).numpy()
print(f"Categorical Cross-Entropy Loss (Keras): {categorical_bce_keras}")
