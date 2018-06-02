import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

T=5.0
Ntm=300
Nsm=100
dt=T/Ntm
W=np.zeros((Ntm+1,Nsm))
Integral=np.zeros((Ntm+1,Nsm))
Exact=np.zeros((Ntm+1,Nsm))
t=np.linspace(0,T,num=Ntm+1)

L2err=np.zeros((Nsm,1))
plt.figure(figsize=(12,6), dpi = 960)
for j in range(0,Nsm):
    for i in range(0,Ntm):
        dW=(np.sqrt(dt))*(np.random.randn(1,1))
        W[i+1,j]=W[i,j]+dW
        Integral[i+1,j]=Integral[i,j]+W[i,j]*dW
        Exact[i+1,j]=0.5*(W[i+1,j]**2)-0.5*i*dt
    plt.plot(t,Exact[:,j],linewidth=.65)
    #err = Integral-Exact
    #L2err[j]=np.mean(err**2)
    #plt.plot(t,Integral,linewidth=.65)

plt.plot(t,-0.5*t,linewidth=2.5,color='#1B9E77')
plt.grid(True)
plt.title('Ito Integral Process Deomo')
plt.grid(True)
plt.xlabel("time") 
plt.ylabel("magnitude")
plt.savefig('./yyfQFdataout/fig1_extact.png', dpi = 960)


T=5.0
Ntms=200
Nin=50

L2err=np.zeros((Ntms,1))
tt=0
Nsm=200
for Ntm in range(Nin, Nin+Ntms):
    dt=T/Ntm
    W=np.zeros((Ntm+1,1))
    Integral=np.zeros((Ntm+1,1))
    Exact=np.zeros((Ntm+1,1))
    t=np.linspace(0,T,num=Ntm+1)
    
    #plt.figure(figsize=(12,6), dpi = 960)
    for j in range(0,Nsm):
        for i in range(0,Ntm):
            dW=(np.sqrt(dt))*(np.random.randn(1,1))
            W[i+1]=W[i]+dW
            Integral[i+1]=Integral[i]+W[i]*dW
            Exact[i+1]=0.5*(W[i+1]**2)-0.5*i*dt
    #plt.plot(t,Exact,linewidth=.65)
    err = Integral-Exact
    #L2err[j]=np.mean(err**2)
    #plt.plot(t,Integral,linewidth=.65)
    L2err[tt]=(Integral[-1]-Exact[-1])**2
    tt=tt+1
    #print(Ntm)


plt.plot(L2err)
#plt.plot(t,-0.5*t,linewidth=2.5,color='#1B9E77')
#plt.grid(True)
#plt.title('Ito Integral Process Deomo')
#plt.grid(True)
#plt.xlabel("time") 
#plt.ylabel("magnitude")
#plt.savefig('fig1_extact.png', dpi = 960)



