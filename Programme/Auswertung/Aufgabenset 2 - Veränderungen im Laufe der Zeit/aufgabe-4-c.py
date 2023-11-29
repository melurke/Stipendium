# comparison of two variables 

import xarray as xr
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# 1a) Pfade der Dateien und Variablenname

infile = "/pfs/work7/workspace/scratch/dp7106-simulierte_welten7/ESCIMO/RC2-base-05/temperature/one_file/tm1_RC2-base-05_195001_209912.nc"
hyam = "hyam"
hybm = "hybm"
aps= 101325
invar = "tm1"

# 1b) Einlesen der Datensätze: Temperaturen und hyam und hybm für die Berechnung der Druckachse

#print('Datensatz 1:')
ds = xr.open_dataset(infile)
data = ds[invar]
hyam = ds[hyam]
hybm = ds[hybm]

#dimension: ('time', 'lev', 'lat', 'lon')

temp=data.values[:,:,::-1,:]

# Zuordnen der Werte zu Längen- und Breitengrad, level indixes, Zeitpunkte

longitudes=data.lon.values
latitudes=data.lat.values[::-1]
levels=data.lev.values
times=data.time.values

#2) Auswahl der Breitengrade, Höhenbereiche und Zeitperioden
#
# Breitengrade: South Pole (SP), index=0
#               Southern High Latitudes (SHL, 90°S-60°S): 0:9
#               Southern Medium Latitudes (SML, 60°S-30°S): 10:20 
#               TROPICS (TRO, 15°S-15°N): 27:36
#               Northern Medium Latidutes (NML, 30°N-60°N): 43:53
#               Northern High Latitudes (NHL, 60°N-90°N): 54:63
#               Norh Pole (NP): 63
#               Global (g) : 0:63
#
# Höhenbereiche: Surface (SF, about 1000 hPa), index=46
#                Troposphere (TR, 1000 to 100 hPa): 21:46
#                Stratosphere (ST, 100 to 1 hPa): 6:20
#                Mesosphere (ME, 1 to 0.01 hPa): 0:5
# 
# Auswahl der Jahre t=0 195001, t=120 196001, t=240 197001, t=360 198001, t=600 200001, t=840 202001, t=1200 205001, t=1800 210001

#Beispiel: global von 1960 bis 2099, Alle 4 Höhenbereiche 
#print('Dimensions')
#print(data.dims)
# global from 1960 to 2100

# dimension temp_zm: ('time', 'lev', 'lat')



minDist = 100
minIndex = -1

for iLat, lat in enumerate(latitudes):
    dist = abs(lat - 8.4)
    if dist < minDist:
        minDist = dist
        minIndex = iLat
    latIndex = minIndex
minDist = 100
minIndex = -1
for iLon, lon in enumerate(longitudes):
    dist = abs(lon - 49.0)
    if dist < minDist:
        minDist = dist
        minIndex = iLon
    lonIndex = minIndex

data = temp[120:1800, 46, latIndex, lonIndex]

# Zeitintervall und Intervall Breitengrade
times=times[120:1800]
Bg='g'
#print('Dimesions new')
#print(data_L.dims)

# Höhenbereiche
Hb='SF'

time_array=np.array(range(0,len(data)))

# calculate the trend coefficients alpha (trend per timestep(month)) and beta (absolute value of trend[0]), 1 stands for linear trend

alpha,beta=np.polyfit(time_array,data,1)

# create fit array for plotting data1 to 4
fit_array=time_array*alpha+beta


fig = plt.figure()
x = np.linspace(1960, 2100, len(data))

plt.plot(x, fit_array, label="Linearer Trend", linewidth=2)
plt.plot(x, data, label="Temperaturen", linewidth=0.8)
plt.xlabel("Zeit")
plt.ylabel("Temperatur [K]")
plt.legend(loc="best")
plt.title("Globaler Temperaturverlauf in der Mesosphäre")
fig.savefig("trends_hoehe/mesosphaere")
plt.show()
plt.close(fig)
