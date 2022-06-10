import pandas as pd

real_estate = pd.read_csv("/home/devuk/code/machine_learning/data/real_estate.csv")

real_estate['monthly_payment'] = 0

#부산 전월세 전환율 지난 1년 평균으로 설정
rent_ratio = 0.06

def deposit_rent(i, deposit, rent) :
    rent_temp = (rent_ratio/12)*deposit
    monthly_payment = rent + rent_temp
    real_estate.monthly_payment[i] = monthly_payment
    

for i in range(len(real_estate)) :
    deposit_rent(i, real_estate.deposit[i], real_estate.rent[i])

real_estate.to_csv("/home/devuk/code/machine_learning/data/real_estate.csv", index = False)