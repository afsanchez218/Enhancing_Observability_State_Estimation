s_new=pd.DataFrame()

s_new['RG60632REA']=np.conjugate(EstimatedAttdfT['IRG60632REA'])*EstimatedAttdfT['V632A']
s_new['RG60632REB']=np.conjugate(EstimatedAttdfT['IRG60632REB'])*EstimatedAttdfT['V632B']
s_new['RG60632REC']=np.conjugate(EstimatedAttdfT['IRG60632REC'])*EstimatedAttdfT['V632C']
s_new['632645SEB']=np.conjugate(EstimatedAttdfT['I632645SEB'])*EstimatedAttdfT['V632B']
s_new['632645SEC']=np.conjugate(EstimatedAttdfT['I632645SEC'])*EstimatedAttdfT['V632C']
s_new['632633SEA']=np.conjugate(EstimatedAttdfT['I632633SEA'])*EstimatedAttdfT['V632A']
s_new['632633SEB']=np.conjugate(EstimatedAttdfT['I632633SEB'])*EstimatedAttdfT['V632B']
s_new['632633SEC']=np.conjugate(EstimatedAttdfT['I632633SEC'])*EstimatedAttdfT['V632C']
s_new['645646REB']=np.conjugate(EstimatedAttdfT['I645646REB'])*EstimatedAttdfT['V646B']
s_new['645646REC']=np.conjugate(EstimatedAttdfT['I645646REC'])*EstimatedAttdfT['V646C']
s_new['633634REA']=np.conjugate(EstimatedAttdfT['I633634REA'])*EstimatedAttdfT['V634A']
s_new['633634REB']=np.conjugate(EstimatedAttdfT['I633634REB'])*EstimatedAttdfT['V634B']
s_new['633634REC']=np.conjugate(EstimatedAttdfT['I633634REC'])*EstimatedAttdfT['V634C']
s_new['671680SEA']=np.conjugate(EstimatedAttdfT['I671680SEA'])*EstimatedAttdfT['V671A']
s_new['671680SEB']=np.conjugate(EstimatedAttdfT['I671680SEB'])*EstimatedAttdfT['V671B']
s_new['671680SEC']=np.conjugate(EstimatedAttdfT['I671680SEC'])*EstimatedAttdfT['V671C']
s_new['671692SEA']=np.conjugate(EstimatedAttdfT['I671692SEA'])*EstimatedAttdfT['V671A']
s_new['671692SEB']=np.conjugate(EstimatedAttdfT['I671692SEB'])*EstimatedAttdfT['V671B']
s_new['671692SEC']=np.conjugate(EstimatedAttdfT['I671692SEC'])*EstimatedAttdfT['V671C']
s_new['671684SEA']=np.conjugate(EstimatedAttdfT['I671684SEA'])*EstimatedAttdfT['V671A']
s_new['671684SEC']=np.conjugate(EstimatedAttdfT['I671684SEC'])*EstimatedAttdfT['V671C']
s_new['692675REA']=np.conjugate(EstimatedAttdfT['I692675REA'])*EstimatedAttdfT['V675A']
s_new['692675REB']=np.conjugate(EstimatedAttdfT['I692675REB'])*EstimatedAttdfT['V675B']
s_new['692675REC']=np.conjugate(EstimatedAttdfT['I692675REC'])*EstimatedAttdfT['V675C']
s_new['684611REC']=np.conjugate(EstimatedAttdfT['I684611REC'])*EstimatedAttdfT['V611C']
s_new['684652REA']=np.conjugate(EstimatedAttdfT['I684652REA'])*EstimatedAttdfT['V652A']
s_new['632671SEA']=np.conjugate(EstimatedAttdfT['I632671SEA'])*EstimatedAttdfT['V632A']
s_new['632671SEB']=np.conjugate(EstimatedAttdfT['I632671SEB'])*EstimatedAttdfT['V632B']
s_new['632671SEC']=np.conjugate(EstimatedAttdfT['I632671SEC'])*EstimatedAttdfT['V632C']
s_new['632671REA']=np.conjugate(EstimatedAttdfT['I632671REA'])*EstimatedAttdfT['V671A']
s_new['632671REB']=np.conjugate(EstimatedAttdfT['I632671REB'])*EstimatedAttdfT['V671B']
s_new['632671REC']=np.conjugate(EstimatedAttdfT['I632671REC'])*EstimatedAttdfT['V671C']

s_new['RG60632SEA']=np.conjugate(Data_Attacked_Copy['IRG60632SEA'])*Data_Attacked_Copy['VRG60A']
s_new['RG60632SEB']=np.conjugate(Data_Attacked_Copy['IRG60632SEB'])*Data_Attacked_Copy['VRG60B']
s_new['RG60632SEC']=np.conjugate(Data_Attacked_Copy['IRG60632SEC'])*Data_Attacked_Copy['VRG60C']
s_new['632645REB']=np.conjugate(Data_Attacked_Copy['I632645REB'])*Data_Attacked_Copy['V645B']
s_new['632645REC']=np.conjugate(Data_Attacked_Copy['I632645REC'])*Data_Attacked_Copy['V645C']
s_new['632633REA']=np.conjugate(Data_Attacked_Copy['I632633REA'])*Data_Attacked_Copy['V633A']
s_new['632633REB']=np.conjugate(Data_Attacked_Copy['I632633REB'])*Data_Attacked_Copy['V633B']
s_new['632633REC']=np.conjugate(Data_Attacked_Copy['I632633REC'])*Data_Attacked_Copy['V633C']
s_new['645646SEB']=np.conjugate(Data_Attacked_Copy['I645646SEB'])*Data_Attacked_Copy['V645B']
s_new['645646SEC']=np.conjugate(Data_Attacked_Copy['I645646SEC'])*Data_Attacked_Copy['V645C']
s_new['633634SEA']=np.conjugate(Data_Attacked_Copy['I633634SEA'])*Data_Attacked_Copy['V633A']
s_new['633634SEB']=np.conjugate(Data_Attacked_Copy['I633634SEB'])*Data_Attacked_Copy['V633B']
s_new['633634SEC']=np.conjugate(Data_Attacked_Copy['I633634SEC'])*Data_Attacked_Copy['V633C']
s_new['671680REA']=np.conjugate(Data_Attacked_Copy['I671680REA'])*Data_Attacked_Copy['V680A']
s_new['671680REB']=np.conjugate(Data_Attacked_Copy['I671680REB'])*Data_Attacked_Copy['V680B']
s_new['671680REC']=np.conjugate(Data_Attacked_Copy['I671680REC'])*Data_Attacked_Copy['V680C']
s_new['671692REA']=np.conjugate(Data_Attacked_Copy['I671692REA'])*Data_Attacked_Copy['V692A']
s_new['671692REB']=np.conjugate(Data_Attacked_Copy['I671692REB'])*Data_Attacked_Copy['V692B']
s_new['671692REC']=np.conjugate(Data_Attacked_Copy['I671692REC'])*Data_Attacked_Copy['V692C']
s_new['671684REA']=np.conjugate(Data_Attacked_Copy['I671684REA'])*Data_Attacked_Copy['V684A']
s_new['671684REC']=np.conjugate(Data_Attacked_Copy['I671684REC'])*Data_Attacked_Copy['V684C']
s_new['692675SEA']=np.conjugate(Data_Attacked_Copy['I692675SEA'])*Data_Attacked_Copy['V692A']
s_new['692675SEB']=np.conjugate(Data_Attacked_Copy['I692675SEB'])*Data_Attacked_Copy['V692B']
s_new['692675SEC']=np.conjugate(Data_Attacked_Copy['I692675SEC'])*Data_Attacked_Copy['V692C']
s_new['684611SEC']=np.conjugate(Data_Attacked_Copy['I684611SEC'])*Data_Attacked_Copy['V684A']
s_new['684652SEA']=np.conjugate(Data_Attacked_Copy['I684652SEA'])*Data_Attacked_Copy['V684C']