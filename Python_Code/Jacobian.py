import numpy as np

def abcd(parameters, type_of_element, terminal_measured):
    if type_of_element=='Line':
        if terminal_measured=='Receiving':
            a=np.identity(parameters[1].shape[0], dtype=np.complex64) + 0.5*parameters[0]@parameters[1]
            b=parameters[0]
            c=parameters[1] + 0.25*parameters[1]@parameters[0]@parameters[1]
            d=np.identity(parameters[1].shape[0], dtype=np.complex64) + 0.5*parameters[0]@parameters[1]
            abcd=[a, b, c, d]
        elif terminal_measured=='Sending':
            a=np.identity(parameters[1].shape[0], dtype=np.complex64) + 0.5*parameters[0]@parameters[1]
            b=-1*parameters[0]
            c=-1*(parameters[1] + 0.25*parameters[1]@parameters[0]@parameters[1])
            d=np.identity(parameters[1].shape[0], dtype=np.complex64) + 0.5*parameters[0]@parameters[1]
            abcd=[a, b, c, d]
    elif type_of_element=='Transformer':
        if terminal_measured=='Sending':
            a=parameters[1]*np.identity(parameters[0].shape[0], dtype=np.complex64)
            b=parameters[1]*parameters[0]
            c=np.array([[0]])
            d=(1/parameters[1])*np.identity(parameters[0].shape[0], dtype=np.complex64)
            abcd=[a, b, c, d]
    elif type_of_element=='Switch':
        a=np.array([[0]])
        b=np.array([[0]])
        c=np.array([[0]])
        d=parameters
        abcd=[a, b, c, d]
    return abcd

jacobian=np.zeros((42,42), dtype=np.complex64)

#RG60 to 632

abcdRG60632=abcd(Param_RG60632, 'Line', 'Sending')

jacobian[0:3,0:3]=abcdRG60632[0]
jacobian[0:3,3:6]=abcdRG60632[1]
jacobian[3:6,0:3]=abcdRG60632[2]
jacobian[3:6,3:6]=abcdRG60632[3]

del abcdRG60632
#632 to 645

abcd632645=abcd(Param_632645, 'Line', 'Receiving')

jacobian[6:8,6:8]=abcd632645[2]
jacobian[6:8,8:10]=abcd632645[3]

del abcd632645
#632 to 633

abcd632633=abcd(Param_632633, 'Line', 'Receiving')

jacobian[8:11,10:13]=abcd632633[2]
jacobian[8:11,13:16]=abcd632633[3]

#645 to 646

abcd645646=abcd(Param_645646, 'Line', 'Sending')

jacobian[11:13,6:8]=abcd645646[0]
jacobian[11:13,16:18]=abcd645646[1]
jacobian[13:15,6:8]=abcd645646[2]
jacobian[13:15,16:18]=abcd645646[3]

del abcd645646
#633 to 634

abcd633634=abcd(Param_633634, 'Transformer', 'Sending')

jacobian[15:18,10:13]=abcd633634[0]
jacobian[15:18,18:21]=abcd633634[1]
jacobian[18:21,18:21]=abcd633634[3]

del abcd633634
#671 to 680

abcd671680=abcd(Param_671680, 'Line', 'Receiving')

jacobian[21:24,21:24]=abcd671680[0]
jacobian[21:24,24:27]=abcd671680[1]
jacobian[24:27,21:24]=abcd671680[2]
jacobian[24:27,24:27]=abcd671680[3]

del abcd671680
#671 to 692

abcd671692=abcd(Param_671692, 'Switch', 'Receiving')

jacobian[27:30,27:30]=abcd671692[3]

del abcd671692
#671 to 684

abcd671684=abcd(Param_671684, 'Line', 'Receiving')

jacobian[30:32,30:32]=abcd671684[2]
jacobian[30:32,32:34]=abcd671684[3]

del abcd671684
#692 to 675

abcd692675=abcd(Param_692675, 'Line', 'Sending')

jacobian[32:35,34:37]=abcd692675[0]
jacobian[32:35,37:40]=abcd692675[1]
jacobian[35:38,34:37]=abcd692675[2]
jacobian[35:38,37:40]=abcd692675[3]

del abcd692675
#684 to 652

abcd684652=abcd(Param_684652, 'Line', 'Sending')

jacobian[40,30]=abcd684652[0]
jacobian[40,41]=abcd684652[1]
jacobian[41,30]=abcd684652[2]
jacobian[41,41]=abcd684652[3]

del abcd684652
#684 to 611

abcd684611=abcd(Param_684611, 'Line', 'Sending')

jacobian[38,31]=abcd684611[0]
jacobian[38,40]=abcd684611[1]
jacobian[39,31]=abcd684611[2]
jacobian[39,40]=abcd684611[3]