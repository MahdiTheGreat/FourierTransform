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

    return np.array(ar2)

def unitImpulse(a,T):
    ar2=[]

    for t in T:
     if(t==a):ar2.append(1)
     else:ar2.append(0)

    return np.asarray(ar2)


def powMaker(a,ar):
    ar2 = [0 for i in range(0, len(ar))]
    for j in range(0, len(ar)):
     ar2[j] = pow(a,ar[j])
    return np.asarray(ar2)

def conditionalFunc(T):
    ar=[]
    for t in T:
        if t<-1:ar.append(0)
        elif t>=-1 and t<=1:
            ar.append(t)
        else:
            temp=t-1
            ar.append(np.cos(temp))
    return np.asarray(ar)

def absolueExp(t,a):
    return np.exp(np.multiply(-1,np.abs(np.multiply(2,t)+a)))


def sigmaFunc(i,j,func,t):
    ar = [0 for i in range(len(t))]
    for n in range(i,j+1):
        ar=np.add(ar,func(t,n))
    return np.asarray(ar)



def convolution(f1,f2,t,r,step):

    temp=np.zeros(len(t),dtype=float)

    r=np.arange(-r,r+step,step)
    print()


    for k in range(len(r)):

        f1Temp=f1([r[k]])

        tempMinus=t-r[k]

        f2Temp=f2(tempMinus)

        temp=temp+(f1Temp[0]*f2Temp)



    return temp

def plotter(t,f):
    plt.plot(t, f)
    plt.show()
    print()


t=np.arange(-25,26,1)
bound=25

def equation1(t):
    return unitStep(-10,t,1)-unitStep(10,t,1)



def equation2(t):
    return np.power(0.25,t)*(unitStep(-5,t,1)-unitStep(5,t,1))





conv=convolution(equation1,equation2,t,bound,1)


f1=equation1(t)
f2=equation2(t)

plotter(t,conv)


t=np.arange(-15,+15.01,0.1)
bound=15

def equation3(t):
    return unitStep(3,t,1)-unitStep(-3,t,1)

def equation4(t):
    return 0.5*np.exp(2*t)*unitStep(0,t,-1)

conv=convolution(equation3,equation4,t,bound,0.1)


plotter(t,conv)










