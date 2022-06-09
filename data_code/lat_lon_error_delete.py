import pandas as pd

real_estate = pd.read_csv("/home/devuk/code/machine_learning/data/real_estate.csv")

index_lat_0 = real_estate[real_estate['latitude'] == 0].index

real_estate_temp = real_estate.drop(index_lat_0)

for i in real_estate_temp.latitude :
    if(i == 0) :
        print(i)
        
real_estate_temp.to_csv("/home/devuk/code/machine_learning/data/real_estate.csv", index = False)