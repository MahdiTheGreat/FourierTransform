import scipy.io.wavfile as wavRead
import numpy as np
import matplotlib.pyplot as plt
import copy

def intergralReal(T,func,k,d):

    arr=[]
    constant = (1 / (len(T)*d))*d
    #w=(2*np.pi)/len(T)
    w=(2*np.pi)/(len(T)*d)



    for i in range(len(k)):
        kw=np.multiply(k[i],w)
        t=np.multiply(T,kw)
        temp=np.multiply(np.cos(t),func)
        temp=np.multiply(temp,constant)
        arr.append(np.sum(temp))


    return arr


def intergralImag(T, func, k, d):
    arr = []
    constant = (1 / (len(T) * d))*d
    w = (2 * np.pi) / (len(T) * d)

    for i in range(len(k)):
        kw = np.multiply(k[i], w)
        t = np.multiply(T, kw)
        temp = np.multiply(np.sin(t), func)
        temp = np.multiply(temp, constant)
        arr.append(np.sum(temp))

    return arr


d=1/44100
T4=100
T3=100
T2=100
T1=100
Tbonus=10114
k=[i for i in range(0,11)]

wav=wavRead.read("wave4.wav")[1]
t=np.arange(0,500,1)
wav=wav[0:500]
plt.plot(t,wav)
plt.show()
t=np.arange(0,T4,1)
t=np.multiply(t,d)
wav=wav[0:T4]
#plt.plot(t,wav)
#plt.show()
Ak=intergralReal(t,wav,k,d)
Bk=intergralImag(t,wav,k,d)
Ak=np.power(Ak,2)
Bk=np.power(Bk,2)
Ck=Ak+Bk
Ck=np.power(Ck,1/2)
#w = (2 * np.pi) /( T4 * d) this is for when we want to plot based on the fundamental frequency
#k=np.multiply(k,w)
plt.plot(k,Ck,"rd")
plt.show()

wav=wavRead.read("wave3.wav")[1]
t=np.arange(0,500,1)
t=np.multiply(t,d)
wav=wav[0:500]
plt.plot(t,wav)
plt.show()
t=np.arange(0,T3,1)
t=np.multiply(t,d)
wav=wav[0:T3]
#plt.plot(t,wav)
#plt.show()
Ak=intergralReal(t,wav,k,d)
Bk=intergralImag(t,wav,k,d)
Ak=np.power(Ak,2)
Bk=np.power(Bk,2)
Ck=Ak+Bk
Ck=np.power(Ck,1/2)
#w = (2 * np.pi) /( T3 * d)
#k=np.multiply(k,w)
plt.plot(k,Ck,"rd")
plt.show()


wav=wavRead.read("wave2.wav")[1]
t=np.arange(0,500,1)
t=np.multiply(t,d)
wav=wav[0:500]
plt.plot(t,wav)
plt.show()
t=np.arange(0,T2,1)
t=np.multiply(t,d)
wav=wav[0:T2]
#plt.plot(t,wav)
#plt.show()
Ak=intergralReal(t,wav,k,d)
Bk=intergralImag(t,wav,k,d)
Ak=np.power(Ak,2)
Bk=np.power(Bk,2)
Ck=Ak+Bk
Ck=np.power(Ck,1/2)
#w = (2 * np.pi) /( T2 * d)
#k=np.multiply(k,w)
plt.plot(k,Ck,"rd")
plt.show()


wav=wavRead.read("wave1.wav")[1]
t=np.arange(0,500,1)
t=np.multiply(t,d)
wav=wav[0:500]
plt.plot(t,wav)
plt.show()
t=np.arange(0,T1,1)
t=np.multiply(t,d)
wav=wav[0:T1]
#plt.plot(t,wav)
#plt.show()
Ak=intergralReal(t,wav,k,d)
Bk=intergralImag(t,wav,k,d)
Ak=np.power(Ak,2)
Bk=np.power(Bk,2)
Ck=Ak+Bk
Ck=np.power(Ck,1/2)
#w = (2 * np.pi) /( T1 * d)
#k=np.multiply(k,w)
plt.plot(k,Ck,"rd")
plt.show()

wav=wavRead.read("bonus.wav")[1]
t=np.arange(0,500,1)
t=np.multiply(t,d)
tempWav=copy.deepcopy(wav[0:500])
plt.plot(t,tempWav)
plt.show()
t=np.arange(0,Tbonus,1)
t=np.multiply(t,d)
wav=wav[0:Tbonus]
#plt.plot(t,wav)
#plt.show()
Ak=intergralReal(t,wav,k,d)
Bk=intergralImag(t,wav,k,d)
Ak=np.power(Ak,2)
Bk=np.power(Bk,2)
Ck=Ak+Bk
Ck=np.power(Ck,1/2)
#w = (2 * np.pi) /( Tbonus * d)
#k=np.multiply(k,w)
plt.plot(k,Ck,"rd")
plt.show()
print(Ck)
print("done")



