import pandas as pd

real_estate = pd.read_csv("/home/devuk/code/machine_learning/data/real_estate.csv")
real_estate['jeonse_check'] = 0
real_estate['rent_check'] = 0


for i in range(len(real_estate)) :
    if real_estate.deposit_rent[i] == '전세' :
        real_estate.jeonse_check[i] = 1
        
    else :
        if real_estate.deposit_rent[i] == '월세' :
            real_estate.rent_check[i] = 1
            
        else :
            print(i)

real_estate.to_csv("/home/devuk/code/machine_learning/data/real_estate.csv", index = False)