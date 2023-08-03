import numpy as np
import matplotlib.pyplot as plt
import copy

def unitStep(a,ar,tSign=1):
    ar2=[0 for i in range(0,len(ar))]

    if tSign>=0:
     for j in range(0,len(ar)):
         if(ar[j]>=(-1*a)):ar2[j]=1
         else:ar2[j]=0
    else:
     for j in range(0, len(ar)):
         if (ar[j] <=a):
             ar2[j] = 1
         else:
             ar2[j] = 0

    return ar2

def unitImpulse(a,T):
    ar2=[]

    for t in T:
     if(t==a):ar2.append(1)
     else:ar2.append(0)

    return ar2


def powMaker(a,ar):
    ar2 = [0 for i in range(0, len(ar))]
    for j in range(0, len(ar)):
     ar2[j] = pow(a,ar[j])
    return ar2

def conditionalFunc(T):
    ar=[]
    for t in T:
        if t<-1:ar.append(0)
        elif t>=-1 and t<=1:
            ar.append(t)
        else:
            temp=t-1
            ar.append(np.cos(temp))
    return ar

def absolueExp(t,a):
    return np.exp(np.multiply(-1,np.abs(np.multiply(2,t)+a)))


def sigmaFunc(i,j,func,t):
    ar = [0 for i in range(len(t))]
    for n in range(i,j+1):
        ar=np.add(ar,func(t,n))
    return ar

t=np.arange(-10,+10.01,0.01)
x1=np.asarray(unitStep(4,np.array(t),-1))
plt.plot(t,x1)
plt.show()
temp=t*0.5
x2=np.exp(temp)
x3=np.multiply(x1,x2)
print("test")
plt.plot(t,x3)
plt.show()

x3=conditionalFunc(t)
plt.plot(t,x3)
plt.show()

x3=sigmaFunc(-20,20,absolueExp,t)
plt.plot(t,x3)
plt.show()

t=np.arange(-20,+21,1)

x1=np.sin(t*np.pi*2.3)
x2=np.cos(t*np.pi*4.3)
x3=np.add(x1,x2)
plt.plot(t,x3)
plt.show()

x1=np.sin(t*np.pi*4.3)
x2=np.cos(t*np.pi*6.3)
x3=np.add(x1,x2)
plt.plot(t,x3)
plt.show()

x1=unitStep(-3,t)
plt.plot(t,x1)
plt.show()
x2=unitStep(3,t,-1)
plt.plot(t,x2)
plt.show()
x3=np.subtract(x1,x2)
plt.plot(t,x3)
plt.show()
x1=unitImpulse(0,t)
plt.plot(t,x1)
plt.show()
x1=np.multiply(2,copy.deepcopy(x1))
print("test")
x3=np.add(copy.deepcopy(x3),x1)
plt.plot(t,x3)
plt.show()






