Data_Attacked=copy.copy(Measurements_Copy)


Attack=0.8
time01=14400
time02=14700

Attack=1-Attack

Data_Attacked_Aux=Attack*Data_Attacked['I632645REB'][time01:time02]
Data_Attacked['I632645REB'][time01:time02]=Data_Attacked_Aux

Data_Attacked_Aux=Attack*Data_Attacked['I632645REC'][time01:time02]
Data_Attacked['I632645REC'][time01:time02]=Data_Attacked_Aux

Data_Attacked_Aux=Attack*Data_Attacked['V645B'][time01:time02]
Data_Attacked['V645B'][time01:time02]=Data_Attacked_Aux

Data_Attacked_Aux=Attack*Data_Attacked['V645C'][time01:time02]
Data_Attacked['V645C'][time01:time02]=Data_Attacked_Aux

Data_Attacked_Copy=copy.copy(Data_Attacked)

Data_Attacked_Labels=Data_Attacked.columns

Data_Attacked=Data_Attacked.T

Data_Attacked=Data_Attacked.values


testing= pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[10, 11, 12], [13, 14, 15]]),columns=['a', 'b', 'c'])
testing_01=0.95*testing['a'][1:3]
testing['a'][1:3]=testing_01
