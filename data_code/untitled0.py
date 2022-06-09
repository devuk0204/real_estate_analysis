import geopandas as gpd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = 'NanumGothic'
plt.rcParams["figure.figsize"] = (10, 10)

bus_file = "/home/devuk/code/machine_learning/tl_bus_station_info.shp"
bus = gpd.read_file(bus_file)
bus