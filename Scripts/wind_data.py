# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:04:20 2022

@author: wyattpetryshen
"""
#Data Source: https://climate.weather.gc.ca/climate_data/hourly_data_e.html?hlyRange=2014-10-23%7C2022-01-20&dlyRange=2018-10-29%7C2022-01-20&mlyRange=%7C&StationID=52959&Prov=BC&urlExtension=_e.html&searchType=stnProx&optLimit=specDate&Month=6&Day=1&StartYear=1840&EndYear=2019&Year=2021&selRowPerPage=25&Line=2&txtRadius=25&optProxType=navLink&txtLatDecDeg=49.745&txtLongDecDeg=-114.8839&timeframe=1
#Sort and Plot Wind Direction and Speed
import pandas as pd
import numpy as np
import os
from windrose import WindroseAxes
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib

os.chdir('PATH') #Input Data Path (Folder containing monthly data)

files = os.listdir() #Delete DS.store file if included in list of files

y2021 = [pd.read_csv(i, sep=",", header = [0])for i in files]

columns = ['Year','Month','Day','Date/Time (LST)','Temp (°C)','Rel Hum (%)',
           'Wind Dir (10s deg)', 'Wind Spd (km/h)']

df2021 = pd.concat(y2021,ignore_index=True)

df2021 = df2021.sort_values("Date/Time (LST)")
df2021["WD"] = df2021["Wind Dir (10s deg)"] * 10

#FILTERED BY WORKING HOURS ONLY
DT_2021 = df2021
DT_2021["Date/Time (LST)"] = pd.to_datetime(DT_2021["Date/Time (LST)"])

DT_2021 = DT_2021.set_index("Date/Time (LST)")
DT_2021 = DT_2021.between_time('00:00','23:59') #Select times


#SINGLE YEARLY PLOT
def plot_single(data):

    wd = data["WD"]
    ws = data['Wind Spd (km/h)']

    ax = WindroseAxes.from_ax()
    ax.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
    matplotlib.projections.polar.PolarAxes.set_theta_zero_location(ax, loc="N", offset=0.0)
    matplotlib.projections.polar.PolarAxes.set_theta_direction(ax, direction=-1)
    matplotlib.projections.polar.PolarAxes.set_thetagrids(ax, angles=[0,45,90,135,180,225,270,315], labels=["N","NE","E","SE","S","SW","W","NW"], fmt='str')
    return

plot_single(df2021)

#MONTHLY SUBPLOTS
def plot_multi(data, time):
    name_add = str(time)
    nrows, ncols = 3, 4
    fig = plt.figure()

    year = 2021
    month = [1,2,3,4,5,6,7,8,9,10,11,12]

    fig.suptitle(f"Wind Speed - {year} - {name_add}")
    for month in range(1, 13):
        ax = fig.add_subplot(nrows, ncols, month, projection="windrose")
        title = datetime(year, month, 1).strftime("%b")
        ax.set_title(title)


        direction = data[data.loc[:,'Month'] == month]["WD"]
        var = data[data.loc[:,'Month'] == month]["Wind Spd (km/h)"]

        ax.bar(direction, var, nsector= 36,opening=0.94, bins=np.arange(0, 31, 5),edgecolor='gray',lw=0.1)
        matplotlib.projections.polar.PolarAxes.set_theta_zero_location(ax, loc="N", offset=0.0)
        matplotlib.projections.polar.PolarAxes.set_theta_direction(ax, direction=-1)
        matplotlib.projections.polar.PolarAxes.set_thetagrids(ax, angles=[0,45,90,135,180,225,270,315], labels=["N","NE","E","SE","S","SW","W","NW"], fmt='str')
    plt.subplots_adjust(wspace = 0.4, hspace = 0.4)
    plt.show()
    return

plot_multi(DT_2021, '00:00 to 23:59')
