import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

Nsim=15000;
aa=np.random.randn(Nsim,1)

accum_a= np.zeros((Nsim, 1))
accum_a[0]=aa[0]
for i in range(1,Nsim):
    accum_a[i]=np.sum(aa[0:i])

plt.plot(accum_a,color = '#1B9E77', linewidth=1.5)
plt.title('Winner Process')
plt.grid(True)
plt.xlabel("time")
plt.ylabel("magnitude")
