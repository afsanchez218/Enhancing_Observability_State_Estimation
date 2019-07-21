import matplotlib.pyplot as plt
x=np.arange(1,(s_ref.shape[0]+1),1)
dfcol=list(s_ref.columns.values)
for n in range(0,len(s_ref.columns)):
    l=[]
    if dfcol[n] != 0:
        aux=dfcol[n][:-1]   
        for m in range(0,len(s_ref.columns)):
            if dfcol[m] != 0 and aux==dfcol[m][:-1]:
                l.append(m)
                dfcol[m]=0
    for w in range(0,len(l)):
        y_real=s_ref.iloc[:,l[w]].real
        lab_y_real=s_ref.columns[l[w]]+'_real (MW)'
        y_imag=s_ref.iloc[:,l[w]].imag
        lab_y_imag=s_ref.columns[l[w]]+'_imag (MVar)'
        plt.plot(x, y_real, label=lab_y_real)
        plt.plot(x, y_imag, label=lab_y_imag)
    if len(l) != 0:
        plt.xlabel('Time (seg)')
        plt.ylabel('S (Apparent Power)')    
        plt.legend(loc=1)
        name=s_ref.columns[l[0]][:-1]+'.jpg'
        plt.savefig(name)
        plt.clf()