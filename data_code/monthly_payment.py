import pandas as pd
import numpy as np

real_estate = pd.read_csv("/home/devuk/code/machine_learning/data/real_estate.csv")

real_estate['monthly_payment'] = 0

#부산 전월세 전환율 지난 1년 평균으로 설정
rent_ratio = 0.06

def deposit_rent(deposit) :
    rent = (rent_ratio/12)*(deposit - 1000)
    return rent

def rent_rent() :
    return rent_ratio

rent = deposit_rent(12000)
print(rent)