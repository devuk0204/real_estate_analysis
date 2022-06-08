import pandas as pd

real_estate = pd.read_csv("/home/devuk/code/machine_learning/data/real_estate.csv")

real_estate['latitude'] = 0
real_estate['longitude'] = 0

real_estate.to_csv("/home/devuk/code/machine_learning/data/real_estate.csv")