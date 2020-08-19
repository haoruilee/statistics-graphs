import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline, BSpline
from matplotlib.pyplot import MultipleLocator
#%matplotlib inline


df=pd.read_csv('pred_r.csv')
df2=pd.read_csv('real_r.csv')
#print(df)
x=list(range(len(df)))
datelist=list()
datelist2=list()
L = df['date']
#创建一个空字典
d = {}
L = d.fromkeys(L)
L = L.keys()
L = list(L)

for j in L:
    #plt.subplot(211)
    x_major_locator=MultipleLocator(30)
    #把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator=MultipleLocator(1)
    #把y轴的刻度间隔设置为10，并存在变量里
    datelist=list()
    datelist2=list()
    for i in x:
        if (df['date'][i]==j):
            datelist.append(df['rank'][i])
    for i in x:
        if (df2['date'][i]==j):
            datelist2.append(df2['rank'][i])
    #x=np.array(x)
    #xnew = np.linspace(x.min(), x.max(), 300) 
    simple_x=np.array(list(range(len(datelist))))
    simple_x2=np.array(list(range(len(datelist2))))
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    ax1.plot(simple_x,datelist,label="pred of {}".format(j))
    ax2 = ax1.twinx()
    ax2.plot(simple_x2,datelist2,label="real of {}".format(j),color='red',linewidth=2.0,linestyle='--')

    # ADD THIS LINE
    ax2.set_yticks(np.linspace(ax2.get_yticks()[0], ax2.get_yticks()[-1], len(ax1.get_yticks())))
 
    fig.legend(loc="lower right")
    #print(datelist)
    #plt.plot(xnew, power_smooth)
    plt.show()
