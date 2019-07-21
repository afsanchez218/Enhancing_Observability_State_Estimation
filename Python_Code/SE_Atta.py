EstimatedAtt=jacobian@Data_Attacked
EstimatedAttdf=pd.DataFrame(EstimatedAtt)
EstimatedAttdf.rename(index={0:'V632A', 1:'V632B', 2:'V632C', 3:'IRG60632REA', 4:'IRG60632REB', 5:'IRG60632REC', 6:'I632645SEB', 7:'I632645SEC', 8:'I632633SEA', 9:'I632633SEB', 10:'I632633SEC', 11:'V646B', 12:'V646C', 13:'I645646REB', 14:'I645646REC', 15:'V634A', 16:'V634B', 17:'V634C', 18:'I633634REA', 19:'I633634REB', 20:'I633634REC', 21:'V671A', 22:'V671B', 23:'V671C', 24:'I671680SEA', 25:'I671680SEB', 26:'I671680SEC', 27:'I671692SEA', 28:'I671692SEB', 29:'I671692SEC', 30:'I671684SEA', 31:'I671684SEC', 32:'V675A', 33:'V675B', 34:'V675C', 35:'I692675REA', 36:'I692675REB', 37:'I692675REC', 38:'V611C', 39:'I684611REC', 40:'V652A', 41:'I684652REA'}, inplace=True)
EstimatedAttdfT=EstimatedAttdf.T

EstimatedAttdfT['I632671SEA']=EstimatedAttdfT['IRG60632REA']-EstimatedAttdfT['I632633SEA']
EstimatedAttdfT['I632671SEB']=EstimatedAttdfT['IRG60632REB']-EstimatedAttdfT['I632633SEB']-EstimatedAttdfT['I632645SEB']
EstimatedAttdfT['I632671SEC']=EstimatedAttdfT['IRG60632REC']-EstimatedAttdfT['I632633SEC']-EstimatedAttdfT['I632645SEC']


EstimatedAttdfT['I632671REA']=EstimatedAttdfT['I671680SEA']-EstimatedAttdfT['I671692SEA']-EstimatedAttdfT['I671684SEA']
EstimatedAttdfT['I632671REB']=EstimatedAttdfT['I671680SEB']-EstimatedAttdfT['I671692SEB']
EstimatedAttdfT['I632671REC']=EstimatedAttdfT['I671680SEC']-EstimatedAttdfT['I671692SEC']-EstimatedAttdfT['I671684SEC']