time01=14400
time02=14700

Data_With_Replacement=copy.copy(Data_Attacked_Copy)

Data_With_Replacement['V645B'][time01:time02]=PM632645REdf['PMV645B']
Data_With_Replacement['V645C'][time01:time02]=PM632645REdf['PMV645C']
Data_With_Replacement['I632645REB'][time01:time02]=PM632645REdf['PMI632645REB']
Data_With_Replacement['I632645REC'][time01:time02]=PM632645REdf['PMI632645REC']



Data_With_Replacement_Copy=copy.copy(Data_With_Replacement)

Data_With_Replacement_Labels=Data_With_Replacement.columns

Data_With_Replacement=Data_With_Replacement.T

Data_With_Replacement=Data_With_Replacement.values