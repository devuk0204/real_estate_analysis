import pandas as pd

"""
cvs_711 = pd.read_csv("/home/devuk/code/machine_learning/data/7eleven_cvs_location.csv")
cvs_gs = pd.read_csv("/home/devuk/code/machine_learning/data/gs_cvs_location.csv")
cvs_cu = pd.read_csv("/home/devuk/code/machine_learning/data/cu_cvs_location.csv")
cvs_ministop = pd.read_csv("/home/devuk/code/machine_learning/data/ministop_cvs_location.csv")
cvs_emart24 = pd.read_csv("/home/devuk/code/machine_learning/data/emart24_cvs_location.csv")

cvs_all = pd.concat([cvs_711, cvs_gs, cvs_cu, cvs_ministop, cvs_emart24], ignore_index= True)
print(cvs_all)
cvs_all.to_csv("/home/devuk/code/machine_learning/data/cvs_location.csv")
"""

apartment = pd.read_csv("/home/devuk/code/machine_learning/data/apartment.csv")
officetel = pd.read_csv("/home/devuk/code/machine_learning/data/officetel.csv")
detatched_multiFamily = pd.read_csv("/home/devuk/code/machine_learning/data/detatched_multiFamily.csv")
row_multiFamily = pd.read_csv("/home/devuk/code/machine_learning/data/row_multiFamily.csv")

apartment_temp = apartment.drop(['floor'], axis = 1)
officetel_temp = officetel.drop(['floor'], axis = 1)
detatched_multiFamily_temp = detatched_multiFamily.drop(['address2'], axis = 1)
row_multiFamily_temp = row_multiFamily.drop(['floor'], axis = 1)

real_estate = pd.concat([apartment_temp, officetel_temp, detatched_multiFamily_temp, row_multiFamily_temp
                         ], ignore_index = True)

real_estate.to_csv("/home/devuk/code/machine_learning/data/real_estate.csv")