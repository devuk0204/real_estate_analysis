import pandas as pd
from haversine import haversine

cvs = pd.read_csv("/home/devuk/code/machine_learning/data/cvs_location_final.csv")
hospital = pd.read_csv("/home/devuk/code/machine_learning/data/hospital.csv")
subway = pd.read_csv("/home/devuk/code/machine_learning/data/subway.csv")
real_estate = pd.read_csv("/home/devuk/code/machine_learning/data/real_estate.csv")

real_estate_temp = real_estate.copy()

def cvs_distance(count) :
    n_cvs = [10000, '']
    estate_crd = (real_estate.latitude[count], real_estate.longitude[count])
    for i in range(len(cvs)) :
        cvs_crd = (cvs.latitude[i], cvs.longitude[i])
        distance = haversine(estate_crd, cvs_crd, unit = 'm')
        distance = round(distance)
        
        if distance < n_cvs[0] :
            n_cvs[0] = distance
            n_cvs[1] = cvs.cvs[i]
            print(i, n_cvs)
    
    real_estate_temp.nearest_cvs[count] = n_cvs[1]
    real_estate_temp.cvs_distance[count] = n_cvs[0]
    
def hospital_distance(count) :
    n_hospital = [100000, '']
    estate_crd = (real_estate.latitude[count], real_estate.longitude[count])
    for i in range(len(hospital)) :
        hospital_crd = (hospital.latitude[i], hospital.longitude[i])
        distance = haversine(estate_crd, hospital_crd, unit = 'm')
        distance = round(distance)
        
        if distance < n_hospital[0] :
            n_hospital[0] = distance
            n_hospital[1] = hospital.hospital_name[i]
            print(i, n_hospital)
    
    real_estate_temp.nearest_hospital[count] = n_hospital[1]
    real_estate_temp.hospital_distance[count] = n_hospital[0]
    
    
def subway_distance(count) :
    n_subway = [100000, '']
    estate_crd = (real_estate.latitude[count], real_estate.longitude[count])
    for i in range(len(subway)) :
        subway_crd = (subway.latitude[i], subway.longitude[i])
        distance = haversine(estate_crd, subway_crd, unit = 'm')
        distance = round(distance)
        
        if distance < n_subway[0] :
            n_subway[0] = distance
            n_subway[1] = subway.station_name[i]
            print(i, n_subway)
    
    real_estate_temp.nearest_station[count] = n_subway[1]
    real_estate_temp.station_distance[count] = n_subway[0]
    
    
for i in range(len(real_estate_temp)) :
    print(i)
    cvs_distance(i)
    hospital_distance(i)
    subway_distance(i)
    
real_estate_temp.to_csv("/home/devuk/code/machine_learning/real_estate.csv")