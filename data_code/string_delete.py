import pandas as pd

#711, gs, cu, ministop -> ( delete
cvs_711 = pd.read_csv("/home/devuk/code/machine_learning/data/7eleven_cvs_location.csv")
cvs_gs = pd.read_csv("/home/devuk/code/machine_learning/data/gs_cvs_location.csv")
cvs_cu = pd.read_csv("/home/devuk/code/machine_learning/data/cu_cvs_location.csv")
cvs_ministop = pd.read_csv("/home/devuk/code/machine_learning/data/ministop_cvs_location.csv")

#emart24 -> | delete
cvs_emart24 = pd.read_csv("/home/devuk/code/machine_learning/data/emart24_cvs_location.csv")



def bracket_delete(cvs) :
    for i in range(len(cvs)) :
        if "(" in cvs.address[i] :
            bracket_index = cvs.address[i].find('(')
            address_temp = cvs.address[i][0:bracket_index]
            cvs.address[i] = address_temp
        print(cvs.address[i])

def rest_delete(cvs) :
    for i in range(len(cvs)) :
        if "," in cvs.address[i] :
            rest_index = cvs.address[i].find(',')
            address_temp = cvs.address[i][0:rest_index]
            cvs.address[i] = address_temp
        print(cvs.address[i])
        
def line_delete(cvs) :
    for i in range(len(cvs)) :
        if "|" in cvs.address[i] :
            rest_index = cvs.address[i].find('|')
            address_temp = cvs.address[i][0:rest_index]
            cvs.address[i] = address_temp
        print(cvs.address[i])
        
rest_delete(cvs_711)        
bracket_delete(cvs_711)
cvs_711.to_csv("/home/devuk/code/machine_learning/data/7eleven_cvs_location.csv", index = False)

rest_delete(cvs_gs)
bracket_delete(cvs_gs)
cvs_gs.to_csv("/home/devuk/code/machine_learning/data/gs_cvs_location.csv", index = False)

rest_delete(cvs_cu)
bracket_delete(cvs_cu)
cvs_cu.to_csv("/home/devuk/code/machine_learning/data/cu_cvs_location.csv", index = False)

rest_delete(cvs_ministop)
bracket_delete(cvs_ministop)
cvs_ministop.to_csv("/home/devuk/code/machine_learning/data/ministop_cvs_location.csv", index = False)

line_delete(cvs_emart24)
bracket_delete(cvs_emart24)
cvs_emart24.to_csv("/home/devuk/code/machine_learning/data/emart24_cvs_location.csv", index = False)