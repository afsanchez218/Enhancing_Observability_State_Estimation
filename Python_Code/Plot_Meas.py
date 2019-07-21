import matplotlib.pyplot as plt
x=np.arange(1,(Measurements_Copy.shape[0]+1),1)
dfcol=list(Measurements_Copy.columns.values)
for n in range(0,len(Measurements_Copy.columns)):
    l=[]
    if dfcol[n] != 0:
        aux=dfcol[n][:-1]   
        for m in range(0,len(Measurements_Copy.columns)):
            if dfcol[m] != 0 and aux==dfcol[m][:-1]:
                l.append(m)
                dfcol[m]=0
    for w in range(0,len(l)):
        y_real=Measurements_Copy.iloc[:,l[w]].real
        lab_y_real=Measurements_Copy.columns[l[w]]+'_real'
        y_imag=Measurements_Copy.iloc[:,l[w]].imag
        lab_y_imag=Measurements_Copy.columns[l[w]]+'_imag'
        plt.plot(x, y_real, label=lab_y_real)
        plt.plot(x, y_imag, label=lab_y_imag)
    if len(l) != 0:
        plt.xlabel('Time (seg)')
        if Measurements_Copy.columns[l[0]][0]=='V':
            plt.ylabel('Voltage (kV)')
        elif Measurements_Copy.columns[l[0]][0]=='I':
            plt.ylabel('Current (kA)')
        plt.legend(loc=1)
        name=Measurements_Copy.columns[l[0]][:-1]+'.jpg'
        plt.savefig(name)
        plt.clf()