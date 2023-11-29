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

temps = []
stds = []

for iLat in range(64):
    averageTemp = 0
    currentTemps = []
    for iTime in range(len(time)):
        for iLon in range(len(longitudes)):
            averageTemp += temp[iTime, 89, iLat, iLon] - 273.15
            currentTemps.append(temp[iTime, 89, iLat, iLon] - 273.15)
    averageTemp /= len(longitudes) * len(time)
    currentTemps = np.array(currentTemps)
    std = np.std(currentTemps)
    temps.append(averageTemp)
    stds.append(std)

plt.plot(np.arange(-90, 90, 2.8125), temps, "-b", label="Durchschnittstemperatur")
plt.plot(np.arange(-90, 90, 2.8125), [temps[i] + stds[i] for i in range(len(temps))], "-g", label="Standardabweichung")
plt.plot(np.arange(-90, 90, 2.8125), [temps[i] - stds[i] for i in range(len(temps))], "-g")
plt.legend(loc="best")
plt.title("Temperaturen der Breitengrade")
plt.xlabel("Breitengrad")
plt.ylabel("Temperatur in °C")
plt.savefig("breitengrade_gesamt.png")
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