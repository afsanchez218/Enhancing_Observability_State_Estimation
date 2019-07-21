###############################################################################
#########  Andres F. Sanchez. Ms Student. Electrical Engineer   ###############
###############################################################################
###############################################################################
import math

voltage_measurements=np.zeros((len(Bus_List_3_Phase),1), dtype=np.complex64)
current_measurements=np.zeros((len(Branch_List_3_Phase),1), dtype=np.complex64)

for n in range(0,Measurements.shape[1]):

    if Measurements[0,n]==1:
        if System[9,n]=='1':
            Aux_V_01=System[3,n]+"_A"
            ind_Aux_V_01=Bus_List_3_Phase.index(Aux_V_01)
            voltage_measurements[ind_Aux_V_01,0]=Measurements[2,n]*((math.cos(math.radians(Measurements[3,n])))+1j*(math.sin(math.radians(Measurements[3,n]))))
        if System[10,n]=='1':
            Aux_V_01=System[3,n]+"_B"
            ind_Aux_V_01=Bus_List_3_Phase.index(Aux_V_01)
            voltage_measurements[ind_Aux_V_01,0]=Measurements[4,n]*((math.cos(math.radians(Measurements[5,n])))+1j*(math.sin(math.radians(Measurements[5,n]))))
        if System[11,n]=='1':
            Aux_V_01=System[3,n]+"_C"
            ind_Aux_V_01=Bus_List_3_Phase.index(Aux_V_01)
            voltage_measurements[ind_Aux_V_01,0]=Measurements[6,n]*((math.cos(math.radians(Measurements[7,n])))+1j*(math.sin(math.radians(Measurements[7,n]))))                                    

    if Measurements[1,n]==1:
        if System[9,n]=='1':
            Aux_Branch_01=(System[2,n]+'_'+System[3,n]+'_A')
            ind_Aux_Branch_01=Branch_List_3_Phase.index(Aux_Branch_01)
            current_measurements[ind_Aux_Branch_01,0]=Measurements[8,n]*((math.cos(math.radians(Measurements[9,n])))+1j*(math.sin(math.radians(Measurements[9,n]))))
        if System[10,n]=='1':
            Aux_Branch_01=(System[2,n]+'_'+System[3,n]+'_B')
            ind_Aux_Branch_01=Branch_List_3_Phase.index(Aux_Branch_01)
            current_measurements[ind_Aux_Branch_01,0]=Measurements[10,n]*((math.cos(math.radians(Measurements[11,n])))+1j*(math.sin(math.radians(Measurements[11,n]))))
        if System[11,n]=='1':
            Aux_Branch_01=(System[2,n]+'_'+System[3,n]+'_C')
            ind_Aux_Branch_01=Branch_List_3_Phase.index(Aux_Branch_01)
            current_measurements[ind_Aux_Branch_01,0]=Measurements[12,n]*((math.cos(math.radians(Measurements[13,n])))+1j*(math.sin(math.radians(Measurements[13,n]))))

measurements_array=np.concatenate((voltage_measurements,current_measurements), axis=0)
        
        
        
        
        if Measurements[n,0]==1:
        Aux_Branch_01=[]
        Aux_V_01=[]
        Aux_V_02=[]
        if System[9,n]=='1':
            Aux_V_01.append(System[2,n]+"_A")
            Aux_V_02.append(System[3,n]+"_A")
            Aux_Branch_01.append(System[2,n]+'_'+System[3,n]+'_A')
        if System[10,n]=='1':
            Aux_V_01.append(System[2,n]+"_B")
            Aux_V_02.append(System[3,n]+"_B")
            Aux_Branch_01.append(System[2,n]+'_'+System[3,n]+'_B')
        if System[11,n]=='1':
            Aux_V_01.append(System[2,n]+"_C")
            Aux_V_02.append(System[3,n]+"_C")
            Aux_Branch_01.append(System[2,n]+'_'+System[3,n]+'_C')