Estimated_Repl=jacobian@Data_With_Replacement
Estimated_Repldf=pd.DataFrame(Estimated_Repl)
Estimated_Repldf.rename(index={0:'V632A', 1:'V632B', 2:'V632C', 3:'IRG60632REA', 4:'IRG60632REB', 5:'IRG60632REC', 6:'I632645SEB', 7:'I632645SEC', 8:'I632633SEA', 9:'I632633SEB', 10:'I632633SEC', 11:'V646B', 12:'V646C', 13:'I645646REB', 14:'I645646REC', 15:'V634A', 16:'V634B', 17:'V634C', 18:'I633634REA', 19:'I633634REB', 20:'I633634REC', 21:'V671A', 22:'V671B', 23:'V671C', 24:'I671680SEA', 25:'I671680SEB', 26:'I671680SEC', 27:'I671692SEA', 28:'I671692SEB', 29:'I671692SEC', 30:'I671684SEA', 31:'I671684SEC', 32:'V675A', 33:'V675B', 34:'V675C', 35:'I692675REA', 36:'I692675REB', 37:'I692675REC', 38:'V611C', 39:'I684611REC', 40:'V652A', 41:'I684652REA'}, inplace=True)
Estimated_RepldfT=Estimated_Repldf.T

Estimated_RepldfT['I632671SEA']=Estimated_RepldfT['IRG60632REA']-Estimated_RepldfT['I632633SEA']
Estimated_RepldfT['I632671SEB']=Estimated_RepldfT['IRG60632REB']-Estimated_RepldfT['I632633SEB']-EstimateddfT['I632645SEB']
Estimated_RepldfT['I632671SEC']=Estimated_RepldfT['IRG60632REC']-Estimated_RepldfT['I632633SEC']-EstimateddfT['I632645SEC']


Estimated_RepldfT['I632671REA']=Estimated_RepldfT['I671680SEA']-Estimated_RepldfT['I671692SEA']-Estimated_RepldfT['I671684SEA']
Estimated_RepldfT['I632671REB']=Estimated_RepldfT['I671680SEB']-Estimated_RepldfT['I671692SEB']
Estimated_RepldfT['I632671REC']=Estimated_RepldfT['I671680SEC']-Estimated_RepldfT['I671692SEC']-Estimated_RepldfT['I671684SEC']

