import matplotlib.pyplot as plt
x=np.arange(1,(EstimateddfT.shape[0]+1),1)
dfcol=list(EstimateddfT.columns.values)
for n in range(0,len(EstimateddfT.columns)):
    l=[]
    if dfcol[n] != 0:
        aux=dfcol[n][:-1]   
        for m in range(0,len(EstimateddfT.columns)):
            if dfcol[m] != 0 and aux==dfcol[m][:-1]:
                l.append(m)
                dfcol[m]=0
    for w in range(0,len(l)):
        y_real=EstimateddfT.iloc[:,l[w]].real
        lab_y_real=EstimateddfT.columns[l[w]]+'_real'
        y_imag=EstimateddfT.iloc[:,l[w]].imag
        lab_y_imag=EstimateddfT.columns[l[w]]+'_imag'
        plt.plot(x, y_real, label=lab_y_real)
        plt.plot(x, y_imag, label=lab_y_imag)
    if len(l) != 0:
        plt.xlabel('Time (seg)')
        if EstimateddfT.columns[l[0]][0]=='V':
            plt.ylabel('Voltage (kV)')
        elif EstimateddfT.columns[l[0]][0]=='I':
            plt.ylabel('Current (kA)')
        plt.legend(loc=1)
        name=EstimateddfT.columns[l[0]][:-1]+'.jpg'
        plt.savefig(name)
        plt.clf()
