#def Calc_Error(Estimated, Validation):
#    Error=[(Estimated-Validation), (100*abs((Estimated-Validation)/Validation))]
#    return Error

def Calc_Error(Estimated, Validation):
    Error=Estimated-Validation
    return Error

def Calc_Error(Estimated, Validation):
    Error=100*abs((Estimated-Validation)/Validation)
    return Error

def Calc_Error(Estimated, Validation, PU_Base):
    Error=(Estimated-Validation)/PU_Base
    return Error