import pandas as pd
import numpy as np
from haversine import haversine

cvs = pd.read_csv("/home/devuk/code/machine_learning/data/cvs_location_final.csv")
hospital = pd.read_csv("/home/devuk/code/machine_learning/data/hospital.csv")
subway = pd.read_csv("/home/devuk/code/machine_learning/data/subway.csv")
real_estate = pd.read_csv("/home/devuk/code/machine_learning/data/real_estate.csv")