import pandas as pd

real_estate = pd.read_csv("/home/devuk/code/machine_learning/data/real_estate.csv")

real_estate['suitability'] = 0

for i in range(len(real_estate)) :
    if real_estate.dedicated_area[i] >= 13.23 :
        if real_estate.cvs_distance[i] <= 500 :
            if real_estate.station_distance[i] <= 1500 :
                if real_estate.hospital_distance[i] <= 5000 :
                    if real_estate.year_of_construction[i] < 2010 :
                        if real_estate.monthly_payment[i] <= 46.5:
                            real_estate.suitability[i] = 1
                        else :
                            real_estate.suitability[i] = 0
                        
                    elif real_estate.year_of_construction[i] >= 2010 :
                        if real_estate.monthly_payment[i] <= 54:
                            real_estate.suitability[i] = 1
                        else :
                            real_estate.suitability[i] = 0
                    
                else :
                    real_estate.suitability[i] = 0
            else :
                real_estate.suitability[i] = 0
        else :
            real_estate.suitability[i] = 0
    else :
        real_estate.suitability[i] = 0
        
count = 0
for i in range(len(real_estate)) :
    if real_estate.suitability[i] == 1 :
        print(i)
        count += 1
print(count)

real_estate.to_csv("/home/devuk/code/machine_learning/data/real_estate.csv")