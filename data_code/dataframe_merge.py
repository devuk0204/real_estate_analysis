import pandas as pd

cvs_711 = pd.read_csv("/home/devuk/code/machine_learning/data/7eleven_cvs_location.csv")
cvs_gs = pd.read_csv("/home/devuk/code/machine_learning/data/gs_cvs_location.csv")
cvs_cu = pd.read_csv("/home/devuk/code/machine_learning/data/cu_cvs_location.csv")
cvs_ministop = pd.read_csv("/home/devuk/code/machine_learning/data/ministop_cvs_location.csv")
cvs_emart24 = pd.read_csv("/home/devuk/code/machine_learning/data/emart24_cvs_location.csv")

cvs_all = pd.concat([cvs_711, cvs_gs, cvs_cu, cvs_ministop, cvs_emart24], ignore_index= True)
print(cvs_all)
cvs_all.to_csv("/home/devuk/code/machine_learning/data/cvs_location.csv")