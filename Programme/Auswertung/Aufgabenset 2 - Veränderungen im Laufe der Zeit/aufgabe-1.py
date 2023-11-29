# comparison of two variables 

import xarray as xr
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def plotten(temp,min_T,max_T,title,title_file,steps):
  fig = plt.figure(figsize=(10,6))
  levels_c=np.arange(min_T,max_T,steps)
  levels_cf=np.linspace(min_T,max_T,50)
  cs=plt.contour(latitudes,press_axis,temp, levels_c, colors='black', linestyles='dashed',linewidths=1.5)
  plt.clabel(cs, inline=True, fontsize=9, fmt='%3i')
  cs2=plt.contourf(latitudes,press_axis,temp, levels_cf, cmap='jet')
  plt.colorbar(cs2)
  #fig.set_ylim(47, 1)
  plt.ylim(1000,0.01)
  plt.yscale('log')
  plt.title(title, fontsize=16)
  plt.xlabel('Latitudes [°N]',fontsize=12)
  #fig.set_ylabel('Levels')
  plt.ylabel('pressure [hPa]',fontsize=12)
  plt.show()
  fig.savefig(title_file)

 
# 1) Pfade der Dateien und Variablenname

#infile = "/pfs/work7/workspace/scratch/dp7106-simulierte_welten6/ESCIMO/RC2-base-06/temperature/tm1_RC2-base-05_195001_209912.nc"
infile ="/pfs/work7/workspace/scratch/dp7106-simulierte_welten7/ESCIMO/RC2-base-05/temperature/one_file/tm1_RC2-base-05_195001_209912.nc"
hyam = "hyam"
hybm = "hybm"
aps= 101325
invar = "tm1"

# 2a) Einlesen der Datensätze: Temperaturen und hyam und hybm für die Berechnung der Druckachse

#print('Datensatz 1:')
ds = xr.open_dataset(infile)
data = ds[invar]
hyam = ds[hyam]
hybm = ds[hybm]

#dimension: ('time', 'lev', 'lat', 'lon')

temp=data.values[:,:,::-1,:]

#print('type data: '+str(type(data1)))
#print('type data')
#print(type(data))
#print('Data values')
#print(data.values)
#print('Dimensions')
#print(data.dims)
#print('Coordinates')
#print(data.coords)
#print('hyam')
#print(hyam)
#print('hybm')
#print(hybm)

# Zuordnen der Werte zu Längen- und Breitengrad, level indixes, Zeitpunkte

longitudes=data.lon.values
latitudes=data.lat.values[::-1]
levels=data.lev.values
times=data.time.values

#print('Levels:')
#for i in range(len(levels)):
#    print(i, ' : ', levels[i])

#print('Latitudes:')
#for i in range(len(latitudes)):
#    print(i, ' : ', latitudes[i])

#print('Longitudes:')
#for i in range(len(longitudes)):
#    print(i, ' : ', longitudes[i])

#print('Time:')
#for i in range(len(times)):
#    print(i, ' : ', times[i])

# 2b) Bestimme Arrays für 2 unterschiedliche Monate (z.B. 209901 und 200001) 
# Auswahl der Jahre t=0 195001, t=120 196001, t=240 197001, t=360 198001, t=600 200001, t=840 202001, t=1200 205001, t=1788 209901 
# dimension: ('time', 'lev', 'lat', 'lon')

date1='197001'
date1_index=1
date2='209901'
date2_index=1788

print('date1: ',times[date1_index])
print('date2: ',times[date2_index])

# zonales Mittel

temp_zm=np.mean(temp,axis=3)

# Zeitintervalle

temp1_zm = temp_zm[date1_index,:,:]
temp2_zm = temp_zm[date2_index,:,:]

# 3) Bestimmung der vertikalen Druckachse mit Hilfe von hyam und hybm

press_axis=hyam+hybm*aps
# Umwandlung von Pa zu hPa bzw. mbar
press_axis=press_axis/100.0
#print('press_axis')
#print(press_axis)
#print('level axis')
#print(levels)

# 4) Ertellen eines Temperatur-Plots mit x-Koordinate Breitengrad und y-Koordinate Höhe in Druck
# a) 1. Zeitpunkt

min_T=np.floor(np.min(temp_zm))
#max_T=np.ceil(max(np.max(temp1_zm),np.max(temp2_zm)))
max_T=np.ceil(np.max(temp_zm))

#for i in range(12):
#	date = str(int(date1)+i)
#	date_index = date1_index + i
#	tempi_zm = temp_zm[date_index,:,:]
#	title='Temperature [K] '+date
#	title_file='temperatur_plots/plots_1970/temp_'+date+'.png'
#
#	steps=10
#
#	plotten(tempi_zm,min_T,max_T,title,title_file,steps)

# b) 2. Zeitpunkt

for i in range(12):	
	date = str(int(date2) + i)
	date_index = date2_index + i
	tempi_zm = temp_zm[date_index,:,:]
	title='Temperature [K] '+date
	title_file='temperatur_plots/plots_2099/temp_'+date+'.png'

	steps = 10

	plotten(tempi_zm,min_T,max_T,title,title_file,steps)

# c) Temperaturdifferenz Zeitpunkt2-Zeitpunkt1

#temp_diff=temp2_zm-temp1_zm
#min_T=np.floor(np.min(temp_diff))
#max_T=np.ceil(np.max(temp_diff))
#steps=2
#print('min_T,max_T',min_T,max_T)

#title='Temperature '+date2+'-'+date1
#title_file='Temp_'+date2+'-'+date1+'.png'

#plotten(temp_diff,min_T,max_T,title,title_file, steps)


