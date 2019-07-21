import numpy as np
import pandas as pd

def abcdv(parameters, type_of_element, terminal_measured):
    if type_of_element=='Line':
        if terminal_measured=='Receiving':
            a=np.identity(parameters[1].shape[0], dtype=np.complex64) + 0.5*parameters[0]@parameters[1]
            b=parameters[0]
            c=parameters[1] + 0.25*parameters[1]@parameters[0]@parameters[1]
            d=np.identity(parameters[1].shape[0], dtype=np.complex64) + 0.5*parameters[0]@parameters[1]
            abcd=[a, b, c, d]
        elif terminal_measured=='Sending':
            a=np.identity(parameters[1].shape[0], dtype=np.complex64) + 0.5*parameters[0]@parameters[1]
            b=-1*parameters[0]
            c=-1*(parameters[1] + 0.25*parameters[1]@parameters[0]@parameters[1])
            d=np.identity(parameters[1].shape[0], dtype=np.complex64) + 0.5*parameters[0]@parameters[1]
            abcd=[a, b, c, d]
    elif type_of_element=='Transformer':
        if terminal_measured=='Sending':
            a=parameters[1]*np.identity(parameters[0].shape[0], dtype=np.complex64)
            b=parameters[1]*parameters[0]
            c=np.array([[0]])
            d=(-1/parameters[1])*np.identity(parameters[0].shape[0], dtype=np.complex64)
            abcd=[a, b, c, d]
    elif type_of_element=='Switch':
        a=np.array([[0]])
        b=np.array([[0]])
        c=np.array([[0]])
        d=parameters
        abcd=[a, b, c, d]
    return abcd

def abcdvm(abcdv):
    abcdvm=np.concatenate((np.concatenate((abcdv[0],abcdv[1]), axis=1), np.concatenate((abcdv[2],abcdv[3]), axis=1)), axis=0)
    return abcdvm

def VI(VI_measurements, abcdvm):
    if VI_measurements.shape[1]==2:
        VI=abcdvm@VI_measurements
    elif VI_measurements.shape[1]==1:
        VI=abcdvm[:,1]@VI_measurements
    return VI

measurements_val=copy.copy(Measurements_Copy)
        
#Test for V632 and IRG60632RE

abcdrg60632=abcdv(Param_RG60632,'Line', 'Sending')

abcdrg60632m=abcdvm(abcdrg60632)

difabcd=abcdrg60632m-jacobian[0:6,0:6]


virg60632=
VRG60A_val=measurements_val['VRG60A'].values.reshape((measurements_val['VRG60A'].values.shape[0],1)).T
VRG60B_val=measurements_val['VRG60B'].values.reshape((measurements_val['VRG60B'].values.shape[0],1)).T
VRG60C_val=measurements_val['VRG60C'].values.reshape((measurements_val['VRG60C'].values.shape[0],1)).T
VRG60_val=np.concatenate((VRG60A_val, VRG60B_val), axis=0)
VRG60_val=np.concatenate((VRG60_val, VRG60C_val), axis=0)



IRG60632SEA_val=measurements_val['IRG60632SEA'].values.reshape((measurements_val['IRG60632SEA'].values.shape[0],1)).T
IRG60632SEB_val=measurements_val['IRG60632SEB'].values.reshape((measurements_val['IRG60632SEB'].values.shape[0],1)).T
IRG60632SEC_val=measurements_val['IRG60632SEC'].values.reshape((measurements_val['IRG60632SEC'].values.shape[0],1)).T
IRG60632SE_val=np.concatenate((IRG60632SEA_val, IRG60632SEB_val), axis=0)
IRG60632SE_val=np.concatenate((IRG60632SE_val, IRG60632SEC_val), axis=0)

V632_Irg60632re=VI(VRG60_val, IRG60632SE_val,abcdrg60val)



Zs=Param_RG60632[0]
Yshunt=Param_RG60632[1]
V_measurements=VRG60
I_measurements=IRG60632SE
Terminal_Measured='Sending'
    
[V632, IRG60632RE]=VI(Param_RG60632[0], Param_RG60632[1], VRG60, IRG60632SE, 'Sending', 'Line')

V632MA=Validation['V632Av'].values.reshape((Validation['V632Av'].values.shape[0],1)).T
V632MB=Validation['V632Bv'].values.reshape((Validation['V632Bv'].values.shape[0],1)).T
V632MC=Validation['V632Cv'].values.reshape((Validation['V632Cv'].values.shape[0],1)).T
V632M=np.concatenate((V632MA, V632MB), axis=0)
V632M=np.concatenate((V632M, V632MC), axis=0)

irg60632reaval=Validation['IRG60632REAv'].values.reshape((Validation['IRG60632REAv'].values.shape[0],1)).T
irg60632rebval=Validation['IRG60632REBv'].values.reshape((Validation['IRG60632REBv'].values.shape[0],1)).T
irg60632recval=Validation['IRG60632RECv'].values.reshape((Validation['IRG60632RECv'].values.shape[0],1)).T
irg60632reval=np.concatenate((irg60632reaval, irg60632rebval), axis=0)
irg60632reval=np.concatenate((irg60632reval, irg60632recval), axis=0)

Error=max(max((abs(V632_Irg60632re[0].real-V632M.real)/(V632M.real))[0]), max(abs((V632_Irg60632re[0].imag-V632M.imag)/(V632M.real))[0]))*100

Error2=max(max((abs(V632_Irg60632re[1].real-irg60632reval.real)/(irg60632reval.real))[0]), max(abs((V632_Irg60632re[1].imag-irg60632reval.imag)/(irg60632reval.imag))[0]))*100