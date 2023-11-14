import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000)
y=0
for k in range(1, 1000, 1):
    y=y+4*np.sin((2*k-1)*x)/((2*k-1)*np.pi)
plt.plot(x,y,'k',color='r',label="w=1",linewidth=3)
plt.axis([0,10,-1.5,1.5])
plt.legend()
plt.show()
