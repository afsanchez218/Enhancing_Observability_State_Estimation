import numpy as np
import os
import h5py
import pandas as pd
import copy


path="C:\\Users\\Felipe_Sanchez\\Thesis_Python_Code"
os.chdir(path)

###############################################################################
################ Measurements Set Import ######################################
#import Data from .mat file provided by RTDS into a pandas DataFrame named
#Measurements

f=h5py.File("Measurements_03.mat",'r')
Data=copy.copy(f['y'])

Vars=list(Data.items())
Data=pd.DataFrame()

for n in range (0,len(Vars)):
    Data[Vars[n][0]]=Vars[n][1][:].T[0].tolist()

f.close()

Measurements=pd.DataFrame()

Measurements['VRG60A']=Data['VRG60Am']*(np.cos(Data['VRG60Aph'])+1j*np.sin(Data['VRG60Aph']))
Measurements['VRG60B']=Data['VRG60Bm']*(np.cos(Data['VRG60Bph'])+1j*np.sin(Data['VRG60Bph']))
Measurements['VRG60C']=Data['VRG60Cm']*(np.cos(Data['VRG60Cph'])+1j*np.sin(Data['VRG60Cph']))

Measurements['IRG60632SEA']=Data['IRG60632SEAm']*(np.cos(Data['IRG60632SEAph'])+1j*np.sin(Data['IRG60632SEAph']))
Measurements['IRG60632SEB']=Data['IRG60632SEBm']*(np.cos(Data['IRG60632SEBph'])+1j*np.sin(Data['IRG60632SEBph']))
Measurements['IRG60632SEC']=Data['IRG60632SECm']*(np.cos(Data['IRG60632SECph'])+1j*np.sin(Data['IRG60632SECph']))

Measurements['V645B']=Data['V645Bm']*(np.cos(Data['V645Bph'])+1j*np.sin(Data['V645Bph']))
Measurements['V645C']=Data['V645Cm']*(np.cos(Data['V645Cph'])+1j*np.sin(Data['V645Cph']))

Measurements['I632645REB']=Data['I632645REBm']*(np.cos(Data['I632645REBph'])+1j*np.sin(Data['I632645REBph']))
Measurements['I632645REC']=Data['I632645RECm']*(np.cos(Data['I632645RECph'])+1j*np.sin(Data['I632645RECph']))

Measurements['V633A']=Data['V633Am']*(np.cos(Data['V633Aph'])+1j*np.sin(Data['V633Aph']))
Measurements['V633B']=Data['V633Bm']*(np.cos(Data['V633Bph'])+1j*np.sin(Data['V633Bph']))
Measurements['V633C']=Data['V633Cm']*(np.cos(Data['V633Cph'])+1j*np.sin(Data['V633Cph']))

Measurements['I632633REA']=-1*Data['I632633REAm']*(np.cos(Data['I632633REAph'])+1j*np.sin(Data['I632633REAph']))
Measurements['I632633REB']=-1*Data['I632633REBm']*(np.cos(Data['I632633REBph'])+1j*np.sin(Data['I632633REBph']))
Measurements['I632633REC']=-1*Data['I632633RECm']*(np.cos(Data['I632633RECph'])+1j*np.sin(Data['I632633RECph']))

Measurements['I645646SEB']=Data['I645646SEBm']*(np.cos(Data['I645646SEBph'])+1j*np.sin(Data['I645646SEBph']))
Measurements['I645646SEC']=Data['I645646SECm']*(np.cos(Data['I645646SECph'])+1j*np.sin(Data['I645646SECph']))

Measurements['I633634SEA']=Data['I633634SEAm']*(np.cos(Data['I633634SEAph'])+1j*np.sin(Data['I633634SEAph']))
Measurements['I633634SEB']=Data['I633634SEBm']*(np.cos(Data['I633634SEBph'])+1j*np.sin(Data['I633634SEBph']))
Measurements['I633634SEC']=Data['I633634SECm']*(np.cos(Data['I633634SECph'])+1j*np.sin(Data['I633634SECph']))

Measurements['V680A']=Data['V680Am']*(np.cos(Data['V680Aph'])+1j*np.sin(Data['V680Aph']))
Measurements['V680B']=Data['V680Bm']*(np.cos(Data['V680Bph'])+1j*np.sin(Data['V680Bph']))
Measurements['V680C']=Data['V680Cm']*(np.cos(Data['V680Cph'])+1j*np.sin(Data['V680Cph']))

Measurements['I671680REA']=-1*Data['I671680REAm']*(np.cos(Data['I671680REAph'])+1j*np.sin(Data['I671680REAph']))
Measurements['I671680REB']=-1*Data['I671680REBm']*(np.cos(Data['I671680REBph'])+1j*np.sin(Data['I671680REBph']))
Measurements['I671680REC']=-1*Data['I671680RECm']*(np.cos(Data['I671680RECph'])+1j*np.sin(Data['I671680RECph']))

Measurements['I671692REA']=Data['I671692REAm']*(np.cos(Data['I671692REAph'])+1j*np.sin(Data['I671692REAph']))
Measurements['I671692REB']=Data['I671692REBm']*(np.cos(Data['I671692REBph'])+1j*np.sin(Data['I671692REBph']))
Measurements['I671692REC']=Data['I671692RECm']*(np.cos(Data['I671692RECph'])+1j*np.sin(Data['I671692RECph']))

Measurements['V684A']=Data['V684Am']*(np.cos(Data['V684Aph'])+1j*np.sin(Data['V684Aph']))
Measurements['V684C']=Data['V684Cm']*(np.cos(Data['V684Cph'])+1j*np.sin(Data['V684Cph']))

Measurements['I671684REA']=Data['I671684REAm']*(np.cos(Data['I671684REAph'])+1j*np.sin(Data['I671684REAph']))
Measurements['I671684REC']=Data['I671684RECm']*(np.cos(Data['I671684RECph'])+1j*np.sin(Data['I671684RECph']))

Measurements['V692A']=Data['V692Am']*(np.cos(Data['V692Aph'])+1j*np.sin(Data['V692Aph']))
Measurements['V692B']=Data['V692Bm']*(np.cos(Data['V692Bph'])+1j*np.sin(Data['V692Bph']))
Measurements['V692C']=Data['V692Cm']*(np.cos(Data['V692Cph'])+1j*np.sin(Data['V692Cph']))

Measurements['I692675SEA']=Data['I692675SEAm']*(np.cos(Data['I692675SEAph'])+1j*np.sin(Data['I692675SEAph']))
Measurements['I692675SEB']=Data['I692675SEBm']*(np.cos(Data['I692675SEBph'])+1j*np.sin(Data['I692675SEBph']))
Measurements['I692675SEC']=Data['I692675SECm']*(np.cos(Data['I692675SECph'])+1j*np.sin(Data['I692675SECph']))

Measurements['I684611SEC']=Data['I684611SECm']*(np.cos(Data['I684611SECph'])+1j*np.sin(Data['I684611SECph']))

Measurements['I684652SEA']=Data['I684652SEAm']*(np.cos(Data['I684652SEAph'])+1j*np.sin(Data['I684652SEAph']))

Measurements=Measurements[['VRG60A', 'VRG60B', 'VRG60C', 'IRG60632SEA', 'IRG60632SEB', 'IRG60632SEC', 'V645B', 'V645C', 'I632645REB', 'I632645REC', 'V633A', 'V633B', 'V633C', 'I632633REA', 'I632633REB', 'I632633REC', 'I645646SEB', 'I645646SEC', 'I633634SEA', 'I633634SEB', 'I633634SEC', 'V680A', 'V680B', 'V680C', 'I671680REA', 'I671680REB', 'I671680REC', 'I671692REA', 'I671692REB', 'I671692REC', 'V684A', 'V684C', 'I671684REA', 'I671684REC', 'V692A', 'V692B', 'V692C', 'I692675SEA', 'I692675SEB', 'I692675SEC', 'I684611SEC', 'I684652SEA']]

Measurements_Copy=copy.copy(Measurements)

Measurements_Labels=Measurements.columns

Measurements=Measurements.T

Measurements=Measurements.values
###############################################################################
################## Validation Set Import ######################################
#import Data from .mat file provided by RTDS into a pandas DataFrame named
#Measurements

f=h5py.File("Validation.mat",'r')
Data=copy.copy(f["Validation"])

Vars=list(Data.items())
Data=pd.DataFrame()

for n in range (0,len(Vars)):
    Data[Vars[n][0]]=Vars[n][1][:].T[0].tolist()

f.close()

Validation=pd.DataFrame()

Validation['V632Av']=Data['V632Am']*(np.cos(Data['V632Aph'])+1j*np.sin(Data['V632Aph']))
Validation['V632Bv']=Data['V632Bm']*(np.cos(Data['V632Bph'])+1j*np.sin(Data['V632Bph']))
Validation['V632Cv']=Data['V632Cm']*(np.cos(Data['V632Cph'])+1j*np.sin(Data['V632Cph']))

Validation['IRG60632REAv']=Data['IRG60632REAm']*(np.cos(Data['IRG60632REAph'])+1j*np.sin(Data['IRG60632REAph']))
Validation['IRG60632REBv']=Data['IRG60632REBm']*(np.cos(Data['IRG60632REBph'])+1j*np.sin(Data['IRG60632REBph']))
Validation['IRG60632RECv']=Data['IRG60632RECm']*(np.cos(Data['IRG60632RECph'])+1j*np.sin(Data['IRG60632RECph']))

Validation['I632645SEBv']=Data['I632645SEBm']*(np.cos(Data['I632645SEBph'])+1j*np.sin(Data['I632645SEBph']))
Validation['I632645SECv']=Data['I632645SECm']*(np.cos(Data['I632645SECph'])+1j*np.sin(Data['I632645SECph']))

Validation['I632671SEAv']=Data['I632671SEAm']*(np.cos(Data['I632671SEAph'])+1j*np.sin(Data['I632671SEAph']))
Validation['I632671SEBv']=Data['I632671SEBm']*(np.cos(Data['I632671SEBph'])+1j*np.sin(Data['I632671SEBph']))
Validation['I632671SECv']=Data['I632671SECm']*(np.cos(Data['I632671SECph'])+1j*np.sin(Data['I632671SECph']))

Validation['I632633SEAv']=Data['I632633SEAm']*(np.cos(Data['I632633SEAph'])+1j*np.sin(Data['I632633SEAph']))
Validation['I632633SEBv']=Data['I632633SEBm']*(np.cos(Data['I632633SEBph'])+1j*np.sin(Data['I632633SEBph']))
Validation['I632633SECv']=Data['I632633SECm']*(np.cos(Data['I632633SECph'])+1j*np.sin(Data['I632633SECph']))

Validation['V646Bv']=Data['V646Bm']*(np.cos(Data['V646Bph'])+1j*np.sin(Data['V646Bph']))
Validation['V646Cv']=Data['V646Cm']*(np.cos(Data['V646Cph'])+1j*np.sin(Data['V646Cph']))

Validation['I645646REBv']=Data['I645646REBm']*(np.cos(Data['I645646REBph'])+1j*np.sin(Data['I645646REBph']))
Validation['I645646RECv']=Data['I645646RECm']*(np.cos(Data['I645646RECph'])+1j*np.sin(Data['I645646RECph']))

Validation['V634Av']=Data['V634Am']*(np.cos(Data['V634Aph'])+1j*np.sin(Data['V634Aph']))
Validation['V634Bv']=Data['V634Bm']*(np.cos(Data['V634Bph'])+1j*np.sin(Data['V634Bph']))
Validation['V634Cv']=Data['V634Cm']*(np.cos(Data['V634Cph'])+1j*np.sin(Data['V634Cph']))

Validation['I633634REAv']=-1*Data['I633634REAm']*(np.cos(Data['I633634REAph'])+1j*np.sin(Data['I633634REAph']))
Validation['I633634REBv']=-1*Data['I633634REBm']*(np.cos(Data['I633634REBph'])+1j*np.sin(Data['I633634REBph']))
Validation['I633634RECv']=-1*Data['I633634RECm']*(np.cos(Data['I633634RECph'])+1j*np.sin(Data['I633634RECph']))

Validation['V671Av']=Data['V671Am']*(np.cos(Data['V671Aph'])+1j*np.sin(Data['V671Aph']))
Validation['V671Bv']=Data['V671Bm']*(np.cos(Data['V671Bph'])+1j*np.sin(Data['V671Bph']))
Validation['V671Cv']=Data['V671Cm']*(np.cos(Data['V671Cph'])+1j*np.sin(Data['V671Cph']))

Validation['I671680SEAv']=Data['I671680SEAm']*(np.cos(Data['I671680SEAph'])+1j*np.sin(Data['I671680SEAph']))
Validation['I671680SEBv']=Data['I671680SEBm']*(np.cos(Data['I671680SEBph'])+1j*np.sin(Data['I671680SEBph']))
Validation['I671680SECv']=Data['I671680SECm']*(np.cos(Data['I671680SECph'])+1j*np.sin(Data['I671680SECph']))

Validation['I671684SEAv']=Data['I671684SEAm']*(np.cos(Data['I671684SEAph'])+1j*np.sin(Data['I671684SEAph']))
Validation['I671684SECv']=Data['I671684SECm']*(np.cos(Data['I671684SECph'])+1j*np.sin(Data['I671684SECph']))

Validation['V675Av']=Data['V675Am']*(np.cos(Data['V675Aph'])+1j*np.sin(Data['V675Aph']))
Validation['V675Bv']=Data['V675Bm']*(np.cos(Data['V675Bph'])+1j*np.sin(Data['V675Bph']))
Validation['V675Cv']=Data['V675Cm']*(np.cos(Data['V675Cph'])+1j*np.sin(Data['V675Cph']))

Validation['I692675REAv']=Data['I692675REAm']*(np.cos(Data['I692675REAph'])+1j*np.sin(Data['I692675REAph']))
Validation['I692675REBv']=Data['I692675REBm']*(np.cos(Data['I692675REBph'])+1j*np.sin(Data['I692675REBph']))
Validation['I692675RECv']=Data['I692675RECm']*(np.cos(Data['I692675RECph'])+1j*np.sin(Data['I692675RECph']))

Validation=Validation[['V632Av', 'V632Bv', 'V632Cv', 'IRG60632REAv', 'IRG60632REBv', 'IRG60632RECv', 'I632645SEBv', 'I632645SECv', 'I632671SEAv', 'I632671SEBv', 'I632671SECv', 'I632633SEAv', 'I632633SEBv', 'I632633SECv', 'V646Bv', 'V646Cv', 'I645646REBv', 'I645646RECv', 'V634Av', 'V634Bv', 'V634Cv', 'I633634REAv', 'I633634REBv', 'I633634RECv', 'V671Av', 'V671Bv', 'V671Cv', 'I671680SEAv', 'I671680SEBv', 'I671680SECv', 'I671684SEAv', 'I671684SECv', 'V675Av', 'V675Bv', 'V675Cv', 'I692675REAv', 'I692675REBv', 'I692675RECv']]




del Vars, n, f, Data
###############################################################################
################### System Elements Paramenter ################################
#LINE PARAMETERS: Line parameters are Zs (series impedance) and
#Yshunt (Shunt admittance). The Parameters are in a list. Position 0 of the
#list is Zs and position 1 of the list is Yshunt. 
#TRANSFORMERS
#
#SWITCH
###############################################################################
##Parameters of Line that starts at bus RG60 and ends at bus 632
RsRG60632=np.array([[0.1312500, 0.0590909, 0.0598485],
                    [0.0590909, 0.1278409, 0.0581439],
                    [0.0598485, 0.0581439, 0.1293182]], dtype=np.complex64)
    
XsRG60632=2j*60*np.pi*np.array([[0.0010228, 0.0005041, 0.0004256],
                            [0.0005041, 0.0010528, 0.0003867],
                            [0.0004256, 0.0003867, 0.0010397]], dtype=np.complex64)
    
GshuntRG60632=np.array([[1/(1e10), 1/(1e10), 1/(1e10)],
                         [1/(1e10), 1/(1e10), 1/(1e10)],
                         [1/(1e10), 1/(1e10), 1/(1e10)]], dtype=np.complex64)
    
BshuntRG60632=np.array([[(2j*np.pi*60*0.00152951e-6), (2j*np.pi*60*0.001002659e-6), (2j*np.pi*60*0.000632753e-6)],
                         [(2j*np.pi*60*0.001002659e-6), (2j*np.pi*60*0.001618783e-6), (2j*np.pi*60*0.000372619e-6)],
                         [(2j*np.pi*60*0.000632753e-6), (2j*np.pi*60*0.000372619e-6), (2j*np.pi*60*0.001827373e-6)]], dtype=np.complex64)

ZsRG60632=RsRG60632+XsRG60632

YshuntRG60632=GshuntRG60632+BshuntRG60632

Param_RG60632=[ZsRG60632, YshuntRG60632]

del RsRG60632, XsRG60632, GshuntRG60632, BshuntRG60632, ZsRG60632, YshuntRG60632
###############################################################################
#Parameters of Line that starts at bus 632 and ends at bus 645

Rs632645=np.array([[0.1258902, 0.0195644],
                   [0.0195644, 0.1253598]], dtype=np.complex64)
    
Xs632645=2j*60*np.pi*np.array([[0.0003384, 0.0001153],
                               [0.0001153, 0.0003408]], dtype=np.complex64)	
    
Bshunt632645=np.array([[(2j*np.pi*60*0.000478496e-6), (2j*np.pi*60*0.000113024e-6)],
                        [(2j*np.pi*60*0.000113024e-6), (2j*np.pi*60*0.000472982e-6)]], dtype=np.complex64)
    
Gshunt632645=np.array([[1/(1e10), 1/(1e10)],
                        [1/(1e10), 1/(1e10)]], dtype=np.complex64)

Zs632645=Rs632645+Xs632645

Yshunt632645=Gshunt632645+Bshunt632645

Param_632645=[Zs632645, Yshunt632645]

del Rs632645, Xs632645, Bshunt632645, Gshunt632645, Zs632645, Yshunt632645 
###############################################################################
#Parameters of Line that starts at bus 645 and ends at bus 646

Rs645646=np.array([[0.0755341, 0.0117386],
                   [0.0117386, 0.0752159]], dtype=np.complex64)
    
Xs645646=2j*60*np.pi*np.array([[0.0002030, 0.0000692],
                               [0.0000692, 0.0002045]], dtype=np.complex64)  
    
Bshunt645646=np.array([[(2j*np.pi*60*0.000287098e-6), (2j*np.pi*60*6.78144e-11)],
                        [(2j*np.pi*60*6.78144e-11), (2j*np.pi*60*0.000283789e-6)]], dtype=np.complex64)
    
Gshunt645646=np.array([[1/(1e10), 1/(1e10)],
                        [1/(1e10), 1/(1e10)]], dtype=np.complex64)

Zs645646=Rs645646+Xs645646

Yshunt645646=Gshunt645646+Bshunt645646

Param_645646=[Zs645646, Yshunt645646]

del Rs645646, Xs645646, Bshunt645646, Gshunt645646, Zs645646, Yshunt645646 
###############################################################################
#Parameters of Line that starts at bus 632 and ends at bus 633

Rs632633=np.array([[0.0712689, 0.0149621, 0.0147727],
                   [0.0149621, 0.0707860, 0.0145360],
                   [0.0147727, 0.0145360, 0.0704167]], dtype=np.complex64)
Xs632633=2j*60*np.pi*np.array([[0.0002968, 0.0001064, 0.0001260],
                               [0.0001064, 0.0003010, 0.0000967],
                               [0.0001260, 0.0000967, 0.0003042]], dtype=np.complex64)
	
Bshunt632633=np.array([[(2j*np.pi*60*0.000367595e-6), (2j*np.pi*60*0.000135857e-6), (2j*np.pi*60*0.00021232e-6)],
                        [(2j*np.pi*60*0.000135857e-6), (2j*np.pi*60*0.000431925e-6), (2j*np.pi*60*8.27427e-11)],
                        [(2j*np.pi*60*0.00021232e-6), (2j*np.pi*60*8.27427e-11), (2j*np.pi*60*0.001827373e-6)]], dtype=np.complex64)

Gshunt632633=np.array([[1/(1e10), 1/(1e10), 1/(1e10)],
                        [1/(1e10), 1/(1e10), 1/(1e10)],
                        [1/(1e10), 1/(1e10), 1/(1e10)]], dtype=np.complex64)

Zs632633=Rs632633+Xs632633

Yshunt632633=Gshunt632633+Bshunt632633

Param_632633=[Zs632633, Yshunt632633]

del Rs632633, Xs632633, Bshunt632633, Gshunt632633, Zs632633, Yshunt632633
###############################################################################
#Parameters of the Transformer that starts at bus 633 and ends at bus 634
#To calculate Z in regular units is used the voltage base of the low voltage 
#side

Z633634pu=np.array([[0.011+0.02j, 0, 0],
                    [0, 0.011+0.02j, 0],
                    [0, 0, 0.011+0.02j]], dtype=np.complex64)
    
S633634base=500000/3

V633634LNbase=480

Z633634base=(V633634LNbase**2)/(S633634base)

Z633634=Z633634base*Z633634pu

nt=(480/4160)+0.0j

Param_633634=[Z633634, nt]

del Z633634pu, S633634base, V633634LNbase, Z633634base, Z633634, nt
###############################################################################
#Parameters of Line that starts at bus 632 and ends at bus 671

Rs632671_01=np.array([[0.0328125, 0.0147727, 0.0149621],
                      [0.0147727, 0.0319602, 0.0145360],
                      [0.0149621, 0.0145360, 0.0323295]], dtype=np.complex64)

Rs632671_02=np.array([[0.0984375, 0.0443182, 0.0448864],
                      [0.0443182, 0.0958807, 0.0436080],
                      [0.0448864, 0.0436080, 0.0969886]], dtype=np.complex64)
    
Xs632671_01=2j*60*np.pi*np.array([[0.0002557, 0.0001260, 0.0001064],
                                  [0.0001260, 0.0002632, 0.0000967],
                                  [0.0001064, 0.0000967, 0.0002599]], dtype=np.complex64)
    
Xs632671_02=2j*60*np.pi*np.array([[0.0007671, 0.0003781, 0.0003192],
                                  [0.0003781, 0.0007896, 0.0002901],
                                  [0.0003192, 0.0002901, 0.0007798]], dtype=np.complex64)

Bshunt632671_01=2j*np.pi*60e-6*np.array([[0.0003823775, 0.0002506650, 0.0001581885],
                                         [0.0002506650, 0.0004046960, 0.0000931545],
                                         [0.0001581885, 0.0000931545, 0.0004568435]], dtype=np.complex64)

Bshunt632671_02=2j*np.pi*60e-6*np.array([[0.001147132, 0.000751994, 0.000474565],
                                         [0.000751994, 0.001214088, 0.000279464],
                                         [0.000474565, 0.000279464, 0.001370530]], dtype=np.complex64)

Gshunt632671=np.array([[1/(1e10), 1/(1e10), 1/(1e10)],
                        [1/(1e10), 1/(1e10), 1/(1e10)],
                        [1/(1e10), 1/(1e10), 1/(1e10)]], dtype=np.complex64)
    
Rs632671=Rs632671_01+Rs632671_02

Xs632671=Xs632671_01+Xs632671_02

Bshunt632671=Bshunt632671_01+Bshunt632671_02

Zs632671=Rs632671+Xs632671

Yshunt632671=Gshunt632671+Bshunt632671

Param_632671=[Zs632671, Yshunt632671]

del Rs632671_01, Rs632671_02, Xs632671_01, Xs632671_02, Bshunt632671_01, Bshunt632671_02, Gshunt632671, Rs632671, Xs632671, Bshunt632671, Zs632671, Yshunt632671
###############################################################################
#Parameters of Line that starts at bus 671 and ends at bus 680

Rs671680=np.array([[0.0656250, 0.0295455, 0.0299242],
                   [0.0295455, 0.0639205, 0.0290720],
                   [0.0299242, 0.0290720, 0.0646591]], dtype= np.complex64)

Xs671680=2j*np.pi*60*np.array([[0.0005114, 0.0002520, 0.0002173],
                               [0.0002520, 0.0005264, 0.0001934],
                               [0.0002173, 0.0001934, 0.0005199]], dtype=np.complex64)

Bshunt671680=2j*np.pi*60e-6*np.array([[0.000764755, 0.00050133, 0.000316377],
                                      [0.00050133, 0.000809392, 0.000186309],
                                      [0.000316377, 0.000186309, 0.000913687]], dtype=np.complex64)

Gshunt671680=np.array([[1/(1e10), 1/(1e10), 1/(1e10)],
                        [1/(1e10), 1/(1e10), 1/(1e10)],
                        [1/(1e10), 1/(1e10), 1/(1e10)]], dtype=np.complex64)

Zs671680=Rs671680+Xs671680

Yshunt671680=Bshunt671680+Gshunt671680

Param_671680=[Zs671680, Yshunt671680]

del Rs671680, Xs671680, Bshunt671680, Gshunt671680, Zs671680, Yshunt671680
###############################################################################
#Parameters of Line that starts at bus 671 and ends at bus 684

Rs671684=np.array([[0.0752159, 0.0117386],
                   [0.0117386, 0.0755341]], dtype=np.complex64)

Xs671684=2j*np.pi*60*np.array([[0.0002045, 0.0000692],
                               [0.0000692, 0.0002030]], dtype=np.complex64)
    
Bshunt671684=2j*np.pi*60e-6*np.array([[0.000283789, 6.78144e-5],
                                      [6.78144e-5, 0.000287098]], dtype=np.complex64)

Gshunt671684=np.array([[1/(1e10), 1/(1e10)],
                        [1/(1e10), 1/(1e10)]], dtype=np.complex64)
    
Zs671684=Rs671684+Xs671684

Yshunt671684=Bshunt671684+Gshunt671684

Param_671684=[Zs671684, Yshunt671684]

del Rs671684, Xs671684, Bshunt671684, Gshunt671684, Zs671684, Yshunt671684
###############################################################################
#Parameters of Line that starts at bus 671 and ends at bus 684

Param_671692=np.identity(3, dtype=np.complex64)
###############################################################################
#Parameters of Line that starts at bus 692 and ends at bus 675

Rs692675=np.array([[0.0755871, 0.0302273, 0.0269792],
                   [0.0302273, 0.0747254, 0.0302273],
                   [0.0269792, 0.0302273, 0.0755871]], dtype=np.complex64)

Xs692675=2j*np.pi*60*np.array([[0.0001121, 0.0000082, 0.0000036],
                               [0.0000082, 0.0001015, 0.0000082],
                               [0.0000036, 0.0000082, 0.0001121]], dtype=np.complex64)

Bshunt692675=2j*np.pi*60e-6*np.array([[0.012168971, 0, 0],
                                      [0, 0.012268971, 0],
                                      [0, 0, 0.012168971]], dtype=np.complex64)

Gshunt692675=np.array([[1/(1e10), 1/(1e10), 1/(1e10)],
                        [1/(1e10), 1/(1e10), 1/(1e10)],
                        [1/(1e10), 1/(1e10), 1/(1e10)]], dtype=np.complex64)

Zs692675=Rs692675+Xs692675

Yshunt692675=Bshunt692675 + Gshunt692675

Param_692675=[Zs692675, Yshunt692675]

del Rs692675, Xs692675, Bshunt692675, Gshunt692675, Zs692675, Yshunt692675
###############################################################################
#Parameters of line that starts at bus 684 and ends at bus 611

Rs684611=np.array([[0.0755227]], dtype=np.complex64)

Xs684611=2j*np.pi*60*np.array([[0.0002031]], dtype=np.complex64)

Bshunt684611=2j*np.pi*60e-6*np.array([[0.0006811]], dtype=np.complex64)

Gshunt684611=np.array([[1/(1e10)]], dtype=np.complex64)

Zs684611=Rs684611+Xs684611

Yshunt684611=Bshunt684611+Gshunt684611

Param_684611=[Zs684611, Yshunt684611]

del Rs684611, Xs684611, Bshunt684611, Gshunt684611, Zs684611, Yshunt684611
###############################################################################
#Parameters of line that starts at bus 684 and ends at bus 652

Rs684652=np.array([[0.2034091]], dtype=np.complex64)

Xs684652=2j*np.pi*60*np.array([[0.0002059]], dtype=np.complex64)

Bshunt684652=2j*np.pi*60e-6*np.array([[0.0357661]], dtype=np.complex64)

Gshunt684652=np.array([[1/(1e10)]], dtype=np.complex64)

Zs684652=Rs684652+Xs684652

Yshunt684652=Bshunt684652+Gshunt684652

Param_684652=[Zs684652, Yshunt684652]

del Rs684652, Xs684652, Bshunt684652, Gshunt684652, Zs684652, Yshunt684652

