import pandas as pd

real_estate = pd.read_csv("/home/devuk/code/machine_learning/data/real_estate.csv")

"""
for i in range(len(real_estate)) :
    if real_estate.type[i] == 'apartment' :
        real_estate.cvs_distance[i] = real_estate.cvs_distance[i] + 150
"""

for i in range(len(real_estate)) :
    if real_estate.type[i] == 'apartment' :
        real_estate.hospital_distance[i] = real_estate.hospital_distance[i] + 150
        real_estate.station_distance[i] = real_estate.station_distance[i] + 150
        
real_estate.to_csv("/home/devuk/code/machine_learning/data/real_estate.csv", index = False)

