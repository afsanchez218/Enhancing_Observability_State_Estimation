s_ref_val=s_ref.values
s_new_val=s_new.values

s_ref_val_real=s_ref_val.real
s_ref_val_imag=s_ref_val.imag

s_new_val_real=s_new_val.real
s_new_val_imag=s_new_val.imag


delta_s_real=s_ref_val_real-s_new_val_real
delta_s_imag=s_ref_val_imag-s_new_val_imag

error_s_real=np.sqrt(delta_s_real**2)
error_s_imag=np.sqrt(delta_s_imag**2)

Att_Detec=np.zeros(error_s_real.shape)

Att_Detec[error_s_real>=0.00025]=1
Att_Detec[error_s_imag>=0.00025]=1

Att_Detect_df=pd.DataFrame(Att_Detec)

Att_Detect_df.rename(columns={0:'RG60632REA',1:'RG60632REB',2:'RG60632REC',3:'632645SEB',4:'632645SEC',5:'632633SEA',6:'632633SEB',7:'632633SEC',8:'645646REB',9:'645646REC',10:'633634REA',11:'633634REB',12:'633634REC',13:'671680SEA',14:'671680SEB',15:'671680SEC',16:'671692SEA',17:'671692SEB',18:'671692SEC',19:'671684SEA',20:'671684SEC',21:'692675REA',22:'692675REB',23:'692675REC',24:'684611REC',25:'684652REA',26:'632671SEA',27:'632671SEB',28:'632671SEC',29:'632671REA',30:'632671REB',31:'632671REC',32:'RG60632SEA',33:'RG60632SEB',34:'RG60632SEC',35:'632645REB',36:'632645REC',37:'632633REA',38:'632633REB',39:'632633REC',40:'645646SEB',41:'645646SEC',42:'633634SEA',43:'633634SEB',44:'633634SEC',45:'671680REA',46:'671680REB',47:'671680REC',48:'671692REA',49:'671692REB',50:'671692REC',51:'671684REA',52:'671684REC',53:'692675SEA',54:'692675SEB',55:'692675SEC',56:'684611SEC',57:'684652SEA'}, inplace=True)



#x=np.arange(1,(Att_Detect_df.shape[0]+1),1)
x=np.arange((time01-10),(time02+10),1)
dfcol=list(Att_Detect_df.columns.values)
for n in range(0,len(Att_Detect_df.columns)):   
    l=[]
    if dfcol[n] != 0:
        aux=dfcol[n][:-1]   
        for m in range(0,len(Att_Detect_df.columns)):
            if dfcol[m] != 0 and aux==dfcol[m][:-1]:
                l.append(m)
                dfcol[m]=0               
    for w in range(0,len(l)):
        #y_Att=Att_Detect_df.iloc[:,l[w]]
        y_Att=Att_Detect_df.iloc[:,l[w]][(time01-10):(time02+10)]
        lab_y_Att=Att_Detect_df.columns[l[w]]
        plt.plot(x, y_Att, label=lab_y_Att)
        
    if len(l) != 0:
        plt.xlabel('Time (seg)')
        plt.ylabel('Error Detection')    
        plt.legend(loc=1)
        name=Att_Detect_df.columns[l[0]][:-1]+'.jpg'
        plt.savefig(name)
        plt.clf()
