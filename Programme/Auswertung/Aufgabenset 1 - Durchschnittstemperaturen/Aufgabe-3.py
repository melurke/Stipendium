import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.dates as mdates
import numpy as np


# 1a) Pfade der Dateien und Variablenname

# on bwUniCluster
infile1 = "/pfs/work7/workspace/scratch/dp7106-simulierte_welten7/T42L90_E5_1979_2021/tm1_ECHAM5_2020.nc"
# for Windows:
#infile1 = "tm1_ECHAM5_2020.nc" 
invar1 = "tm1"

# 1b) Einlesen erster Datensatz

ds = xr.open_dataset(infile1)
data1 = ds[invar1]

# 1c) Umwandluing in NumPy Arrays
#dimension: ('time', 'lev', 'lat', 'lon')
temp=data1.values[:,:,::-1,:]

longitudes=data1.lon.values
latitudes=data1.lat.values[::-1]
levels=data1.lev.values
time=data1.time.values

times = []
for i, t in enumerate(time):
    times.append(i / len(time) * 365)

minIndex = int(input("minIndex: "))
maxIndex = int(input("maxIndex: "))

citiesList = ["Karlsruhe", "Berlin", "Moskau", "Reykjavik", "Peking", "Tefe, Brasilien", "Calgary, Kanada", "Sydney, Australien", "Neumayer-Station, Antarktis"]

cities = {
    "Karlsruhe": [49.0, 8.4],
    "Berlin": [52.5, 13.4],
    "Moskau": [55.8, 37.6],
    "Reykjavik": [64.1, 21.9],
    "Peking": [39.9, 116.4],
    "Tefe, Brasilien": [3.4, 64.7],
    "Calgary, Kanada": [51.1, 114.1],
    "Sydney, Australien": [33.9, 151.2],
    "Neumayer-Station, Antarktis": [70.4, 8.2],
}

for i, city in enumerate(cities.values):
    indices = [0, 0, []]
    minDist = 100
    minIndex = -1
    for iLat, lat in enumerate(latitudes):
        dist = abs(lat - city[1])
        if dist < minDist:
            minDist = dist
            minIndex = iLat
    indices[1] = minIndex
    minDist = 100
    minIndex = -1
    for iLon, lon in enumerate(longitudes):
        dist = abs(lon - city[0])
        if dist < minDist:
            minDist = dist
            minIndex = iLon
    indices[0] = minIndex
    city.extend(indices)

    for t in temp[:, 89, indices[1], indices[0]]:
        city[-1].append(t)
    plt.plot(times, city[-1])
    plt.savefig("staedte/" + citiesList[i].replace(", ", "_").lower() + ".png")
    plt.show()

# Breitengrade: South Pole (SP), index=0
#               Southern High Latitudes (SHL, 90°S-60°S): 0:9
#               Southern Medium Latitudes (SML, 60°S-30°S): 10:20
#               TROPICS (Tropics, 15°S-15°N): 27:36
#               Northern Medium Latidutes (NML, 30°N-60°N): 43:53
#               Northern High Latitudes (NHL, 60°N-90°N): 54:63
#               Norh Pole (NP): 63
#               Global (g) : 0:63
#
# Höhenbereiche: Surface (SF, about 1000 hPa), index=89
#                Troposphere (TR, 1000 to 100 hPa): 63:89
#                Stratosphere (ST, 100 to 1 hPa): 14:62
#                Mesosphere (ME, 1 to 0.01 hPa): 0:13
#