import numpy as np
x = np.array([[0,0],[1,0],[0,1],[1,1]])
out=np.array([0,0,0,1])

wh = np.random.rand(2,3)
bh = np.random.rand(3)

wo=np.random.rand(3,1)
bo=np.random.rand(1)

lr=1.5
epoch = 1000

def acti(z):
    return 1/(1 + np.exp(-z))

def acti_deri(z):
    return z * (1 - z)

def forward(x,wh,bh,wo,bo):
    zh=np.dot(x,wh)+bh   #(1,2)*(2,3)+(3,)=>(1,3)
    ah=acti(zh)
    zo=np.dot(ah,wo)+bo  #(1,3)*(3,1)+(1,)=>(1,1)
    ao=acti(zo)
    return ah,ao

for e in range(epoch):
    tot_err=0
    for i in range(len(x)):
        ah,ao=forward(x[i],wh,bh,wo,bo)
        err=out[i]-ao   # value
        tot_err+=np.sum(err**2)  

        do=err*acti_deri(ao) #(1,1)
        dh=do.dot(wo.T)*acti_deri(ah) # (1,1)*(1,3) to all ele (1,3)=(1,3)

        wo+=lr*ah.reshape(-1,1)*do  # (3,1)*(1,1)=(3,1)
        bo+=lr*do # (1,)
        wh+=lr*x[i].reshape(-1,1)*dh # (2,1)*(1,3)=(2,3)
        bh+=lr*dh # (1,3)

    if epoch % 10 == 0:
        print(f"epoch {e},total trror : {tot_err}")

for i in range(len(x)):
    ah,ao=forward(x[i], wh, bh, wo, bo)
    if ao>=0.5:
        pred=1    
    else:        
        pred=0
    print(f"Input: {x[i]}, Predicted Output: {pred}, Actual Output: {out[i]}")