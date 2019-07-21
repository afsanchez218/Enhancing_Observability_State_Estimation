Estimated=jacobian@Measurements
Estimateddf=pd.DataFrame(Estimated)
Estimateddf.rename(index={0:'V632A', 1:'V632B', 2:'V632C', 3:'IRG60632REA', 4:'IRG60632REB', 5:'IRG60632REC', 6:'I632645SEB', 7:'I632645SEC', 8:'I632633SEA', 9:'I632633SEB', 10:'I632633SEC', 11:'V646B', 12:'V646C', 13:'I645646REB', 14:'I645646REC', 15:'V634A', 16:'V634B', 17:'V634C', 18:'I633634REA', 19:'I633634REB', 20:'I633634REC', 21:'V671A', 22:'V671B', 23:'V671C', 24:'I671680SEA', 25:'I671680SEB', 26:'I671680SEC', 27:'I671692SEA', 28:'I671692SEB', 29:'I671692SEC', 30:'I671684SEA', 31:'I671684SEC', 32:'V675A', 33:'V675B', 34:'V675C', 35:'I692675REA', 36:'I692675REB', 37:'I692675REC', 38:'V611C', 39:'I684611REC', 40:'V652A', 41:'I684652REA'}, inplace=True)
EstimateddfT=Estimateddf.T

EstimateddfT['I632671SEA']=EstimateddfT['IRG60632REA']-EstimateddfT['I632633SEA']
EstimateddfT['I632671SEB']=EstimateddfT['IRG60632REB']-EstimateddfT['I632633SEB']-EstimateddfT['I632645SEB']
EstimateddfT['I632671SEC']=EstimateddfT['IRG60632REC']-EstimateddfT['I632633SEC']-EstimateddfT['I632645SEC']


EstimateddfT['I632671REA']=EstimateddfT['I671680SEA']-EstimateddfT['I671692SEA']-EstimateddfT['I671684SEA']
EstimateddfT['I632671REB']=EstimateddfT['I671680SEB']-EstimateddfT['I671692SEB']
EstimateddfT['I632671REC']=EstimateddfT['I671680SEC']-EstimateddfT['I671692SEC']-EstimateddfT['I671684SEC']


#p.u. Bases

V_Base_01=4.16
V_Base_02=0.48
S_Base_01=5000
S_Base_02=500
I_Base_01=(S_Base_01/V_Base_01)/1000
I_Base_02=(S_Base_02/V_Base_02)/1000