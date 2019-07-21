import numpy as np
import os
import h5py
import pandas as pd
import copy
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture as GMM
from sklearn.preprocessing import scale as scale

path="C:\\Users\\Felipe_Sanchez\\Thesis_Python_Code"
os.chdir(path)

###############################################################################
################ Measurements Set Import ######################################
#import Data from .mat file provided by RTDS into a pandas DataFrame named
#Measurements

f=h5py.File("Pseudo632645RE_04.mat",'r')
Data=copy.copy(f['Pseudo632645RE'])

Vars=list(Data.items())
Data=pd.DataFrame()

for n in range (0,len(Vars)):
    Data[Vars[n][0]]=Vars[n][1][:].T[0].tolist()

f.close()

Pseudo632645RE=copy.copy(Data)

time01=14400
time02=14700
#time01=14400
#time02=14700
PseudoV645BmData=np.array([Pseudo632645RE['V645BmDay01'][time01:time02], 
                            Pseudo632645RE['V645BmDay02'][time01:time02], 
                            Pseudo632645RE['V645BmDay03'][time01:time02], 
                            Pseudo632645RE['V645BmDay04'][time01:time02], 
                            Pseudo632645RE['V645BmDay05'][time01:time02], 
                            Pseudo632645RE['V645BmDay06'][time01:time02], 
                            Pseudo632645RE['V645BmDay07'][time01:time02], 
                            Pseudo632645RE['V645BmDay08'][time01:time02], 
                            Pseudo632645RE['V645BmDay09'][time01:time02], 
                            Pseudo632645RE['V645BmDay10'][time01:time02]])

PseudoV645BphData=np.array([Pseudo632645RE['V645BphDay01'][time01:time02], 
                            Pseudo632645RE['V645BphDay02'][time01:time02], 
                            Pseudo632645RE['V645BphDay03'][time01:time02], 
                            Pseudo632645RE['V645BphDay04'][time01:time02], 
                            Pseudo632645RE['V645BphDay05'][time01:time02], 
                            Pseudo632645RE['V645BphDay06'][time01:time02], 
                            Pseudo632645RE['V645BphDay07'][time01:time02], 
                            Pseudo632645RE['V645BphDay08'][time01:time02], 
                            Pseudo632645RE['V645BphDay09'][time01:time02], 
                            Pseudo632645RE['V645BphDay10'][time01:time02]])
    
PseudoV645CmData=np.array([Pseudo632645RE['V645CmDay01'][time01:time02], 
                            Pseudo632645RE['V645CmDay02'][time01:time02], 
                            Pseudo632645RE['V645CmDay03'][time01:time02], 
                            Pseudo632645RE['V645CmDay04'][time01:time02], 
                            Pseudo632645RE['V645CmDay05'][time01:time02], 
                            Pseudo632645RE['V645CmDay06'][time01:time02], 
                            Pseudo632645RE['V645CmDay07'][time01:time02], 
                            Pseudo632645RE['V645CmDay08'][time01:time02], 
                            Pseudo632645RE['V645CmDay09'][time01:time02], 
                            Pseudo632645RE['V645CmDay10'][time01:time02]])
    
PseudoV645CphData=np.array([Pseudo632645RE['V645CphDay01'][time01:time02], 
                            Pseudo632645RE['V645CphDay02'][time01:time02], 
                            Pseudo632645RE['V645CphDay03'][time01:time02], 
                            Pseudo632645RE['V645CphDay04'][time01:time02], 
                            Pseudo632645RE['V645CphDay05'][time01:time02], 
                            Pseudo632645RE['V645CphDay06'][time01:time02], 
                            Pseudo632645RE['V645CphDay07'][time01:time02], 
                            Pseudo632645RE['V645CphDay08'][time01:time02], 
                            Pseudo632645RE['V645CphDay09'][time01:time02], 
                            Pseudo632645RE['V645CphDay10'][time01:time02]])
    
PseudoI632645REBmData=np.array([Pseudo632645RE['I632645REBmDay01'][time01:time02],
                                Pseudo632645RE['I632645REBmDay02'][time01:time02], 
                                Pseudo632645RE['I632645REBmDay03'][time01:time02],
                                Pseudo632645RE['I632645REBmDay04'][time01:time02],
                                Pseudo632645RE['I632645REBmDay05'][time01:time02],
                                Pseudo632645RE['I632645REBmDay06'][time01:time02],
                                Pseudo632645RE['I632645REBmDay07'][time01:time02],
                                Pseudo632645RE['I632645REBmDay08'][time01:time02],
                                Pseudo632645RE['I632645REBmDay09'][time01:time02],
                                Pseudo632645RE['I632645REBmDay10'][time01:time02]])

PseudoI632645REBphData=np.array([Pseudo632645RE['I632645REBphDay01'][time01:time02],
                                Pseudo632645RE['I632645REBphDay02'][time01:time02], 
                                Pseudo632645RE['I632645REBphDay03'][time01:time02],
                                Pseudo632645RE['I632645REBphDay04'][time01:time02],
                                Pseudo632645RE['I632645REBphDay05'][time01:time02],
                                Pseudo632645RE['I632645REBphDay06'][time01:time02],
                                Pseudo632645RE['I632645REBphDay07'][time01:time02],
                                Pseudo632645RE['I632645REBphDay08'][time01:time02],
                                Pseudo632645RE['I632645REBphDay09'][time01:time02],
                                Pseudo632645RE['I632645REBphDay10'][time01:time02]])
    
PseudoI632645RECmData=np.array([Pseudo632645RE['I632645RECmDay01'][time01:time02],
                                Pseudo632645RE['I632645RECmDay02'][time01:time02], 
                                Pseudo632645RE['I632645RECmDay03'][time01:time02],
                                Pseudo632645RE['I632645RECmDay04'][time01:time02],
                                Pseudo632645RE['I632645RECmDay05'][time01:time02],
                                Pseudo632645RE['I632645RECmDay06'][time01:time02],
                                Pseudo632645RE['I632645RECmDay07'][time01:time02],
                                Pseudo632645RE['I632645RECmDay08'][time01:time02],
                                Pseudo632645RE['I632645RECmDay09'][time01:time02],
                                Pseudo632645RE['I632645RECmDay10'][time01:time02]])

PseudoI632645RECphData=np.array([Pseudo632645RE['I632645RECphDay01'][time01:time02],
                                Pseudo632645RE['I632645RECphDay02'][time01:time02], 
                                Pseudo632645RE['I632645RECphDay03'][time01:time02],
                                Pseudo632645RE['I632645RECphDay04'][time01:time02],
                                Pseudo632645RE['I632645RECphDay05'][time01:time02],
                                Pseudo632645RE['I632645RECphDay06'][time01:time02],
                                Pseudo632645RE['I632645RECphDay07'][time01:time02],
                                Pseudo632645RE['I632645RECphDay08'][time01:time02],
                                Pseudo632645RE['I632645RECphDay09'][time01:time02],
                                Pseudo632645RE['I632645RECphDay10'][time01:time02]])
###############################################################################
#Example to get plot of histogram and gmm
    
xgmm=PseudoI632645REBphData[:,int((time02-time01)/2)]
#xgmm=PseudoI632645REBmData[:,1]  
xgmm=xgmm.reshape(-1,1)

x_aux_min=-0.1*abs(max(xgmm)-min(xgmm))+min(xgmm)
x_aux_max=0.1*abs(max(xgmm)-min(xgmm))+max(xgmm)
x_aux_step=abs(max(xgmm)-min(xgmm))/1000
x_aux=np.arange(x_aux_min,x_aux_max,x_aux_step).reshape(-1,1)

n_comps = np.arange(1, xgmm.shape[0])
models = [GMM(n, covariance_type='full', random_state=0).fit(xgmm) for n in n_comps]

bic=[m.bic(xgmm) for m in models]
aic=[m.aic(xgmm) for m in models]

plt.plot(n_comps,bic)
plt.plot(n_comps,aic)
plt.show
plt.clf()

n_comp=n_comps[np.argmin(aic)]

gmm = GMM(n_components=n_comp, init_params='kmeans').fit(xgmm)

we=gmm.weights_
mean=gmm.means_
cova=gmm.covariances_

prep=np.exp(gmm.score_samples(x_aux))
prepaux=(1/max(prep))*prep

fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Current Phase (rad)')
ax1.set_ylabel('Histogram (Frequency)', color=color)
ax1.hist(xgmm, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('GMM Probability density Function', color=color)
ax2.plot(x_aux, prepaux, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.grid(True)
ax1.grid(True)
plt.show()

maxprob=np.argmax(prep)
pseudo=x_aux[maxprob]
###############################################################################
def Pseudo(Pseudo_Array):
    #PseudoMeasurement=np.zeros([1,PseudoV645BmData.shape[1]])
    #for n in range(0,PseudoV645BmData.shape[1]):
    #    xgmm=PseudoV645BmData[:,n]
    PseudoMeasurement=np.zeros([1,Pseudo_Array.shape[1]])
    for n in range(0,Pseudo_Array.shape[1]):
        xgmm=Pseudo_Array[:,n]
        xgmm=xgmm.reshape(-1,1)
        
        x_aux_min=-0.1*abs(max(xgmm)-min(xgmm))+min(xgmm)
        x_aux_max=0.1*abs(max(xgmm)-min(xgmm))+max(xgmm)
        x_aux_step=abs(max(xgmm)-min(xgmm))/1000
        x_aux=np.arange(x_aux_min,x_aux_max,x_aux_step).reshape(-1,1)
        
        n_comps = np.arange(1, xgmm.shape[0])
        models = [GMM(n, covariance_type='full', random_state=0).fit(xgmm) for n in n_comps]
        aic=[m.aic(xgmm) for m in models]
        n_comp=n_comps[np.argmin(aic)]
        
        gmm = GMM(n_components=n_comp, init_params='kmeans').fit(xgmm)
        prep=np.exp(gmm.score_samples(x_aux))
        
        maxprob=np.argmax(prep)
        PseudoMeasurement[0,n]=x_aux[maxprob]
    return PseudoMeasurement
###############################################################################
PMV645Bm=Pseudo(PseudoV645BmData)
PMV645Bph=Pseudo(PseudoV645BphData)
PMV645Cm=Pseudo(PseudoV645CmData)
PMV645Cph=Pseudo(PseudoV645CphData)

PMI632645REBm=Pseudo(PseudoI632645REBmData)
PMI632645REBph=Pseudo(PseudoI632645REBphData)
PMI632645RECm=Pseudo(PseudoI632645RECmData)
PMI632645RECph=Pseudo(PseudoI632645RECphData)

PM632645REdf=pd.DataFrame()

PM632645REdf['PMV645B']=(PMV645Bm*(np.cos(PMV645Bph)+1j*np.sin(PMV645Bph))).reshape(-1).tolist()
PM632645REdf['PMV645C']=(PMV645Cm*(np.cos(PMV645Cph)+1j*np.sin(PMV645Cph))).reshape(-1).tolist()

PM632645REdf['PMI632645REB']=(PMI632645REBm*(np.cos(PMI632645REBph)+1j*np.sin(PMI632645REBph))).reshape(-1).tolist()
PM632645REdf['PMI632645REC']=(PMI632645RECm*(np.cos(PMI632645RECph)+1j*np.sin(PMI632645RECph))).reshape(-1).tolist()
