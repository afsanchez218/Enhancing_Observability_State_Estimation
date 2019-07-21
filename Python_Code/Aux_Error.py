x1=xx=Error.idxmax(axis=0)
x2=x1.to_frame()
x3=x2.T
x4=np.zeros((len(x3.columns)), dtype=float)
x5=list(x3.columns.values)
for n in range(0,len(x3.columns)):
    x4[n]=Error[x3.columns[n]][int(x3[x3.columns[n]][0])]

x6=pd.DataFrame(x4).T

x6.columns=x5

x7=[x3,x6]

x8=pd.concat(x7, ignore_index=True)