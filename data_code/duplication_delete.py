import pandas as pd

real_estate = pd.read_csv("/home/devuk/code/machine_learning/data/real_estate.csv")


real_estate_temp = real_estate.drop_duplicates(['address1', 'address2', 'dedicated_area(m^2)', 'deposit_rent', 'deposit', 'rent'], keep = 'first')
real_estate_temp.to_csv("/home/devuk/code/machine_learning/data/real_estate.csv", index = False)
