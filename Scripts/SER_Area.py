# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Need attribute values from shape file
import pandas as pd
import re
import numpy as np

#File location of xlsx file
Path = r"/Volumes/GoogleDrive/My Drive/Geoscience:Engineering/High Elevation Grasslands/SER.xlsx"

#Import file
SER = pd.read_excel(Path)

#Search for all occurances of name "Festuca". Edit to change query
fes = SER[SER['Scientific Name Formatted'].str.contains(r'Festuca')]

#Find Percent occurance in Occurance Data Column
O_Percent = []
for i in np.arange(0,len(fes)):
    to_search = fes['Occurrence Data'].iloc[i]
    if re.search("percent", to_search) is None:
        O_Percent.append("")
    else:
        occ_per = to_search[re.search("percent", to_search).span()[0]-5:re.search("percent", to_search).span()[1]]
        O_Percent.append(occ_per)

ser_per = [float(re.sub("[^0-9.]","",i)) for i in O_Percent]

max_area = [re.sub("[^0-9.]","",i) for i in fes['Occurrence Size']]

#Find maximum area in Occurance Size column
m_area = []
for i in np.arange(0,len(max_area)):
    if max_area[i].endswith("."):
        val = max_area[i][:-1]
        m_area.append(val)
    else:
        val = max_area[i]
        m_area.append(val)

m_area = [float(i) for i in m_area]

len(m_area) != len(ser_per)

total_area = []
for i in np.arange(0,len(ser_per)):
    val = (ser_per[i]/100) * m_area[i]
    total_area.append(val)

#Print total areas of query type. Rounded to two decimals
print("Total High Elevation Grasslands: %s ha" % round(sum(total_area),2))


ind = np.where(fes["Shape ID"].reset_index() == 121696)[0][0]

print("Area: %s ha" %round(total_area[ind],2))

#Function of the above steps.
#Data: xlsx file
#Scientific_Name: Name you want to search for
#Polygon: Polygon ID from CDC to include

def return_area(Data,Scientific_Name,Polygons):
    #filer data based on search name
    fes = Data[Data['Scientific Name Formatted'].str.contains(Scientific_Name)]
    #find area
    O_Percent = []
    for i in np.arange(0,len(fes)):
        to_search = fes['Occurrence Data'].iloc[i]
        if re.search("percent", to_search) is None:
            O_Percent.append("")
        else:
            occ_per = to_search[re.search("percent", to_search).span()[0]-5:re.search("percent", to_search).span()[1]]
            O_Percent.append(occ_per)
    #extract percentages
    ser_per = [float(re.sub("[^0-9.]","",i)) for i in O_Percent]
    #extract max area
    max_area = [re.sub("[^0-9.]","",i) for i in fes['Occurrence Size']]
    #remove incorrect characters
    m_area = []
    for i in np.arange(0,len(max_area)):
        if max_area[i].endswith("."):
            val = max_area[i][:-1]
            m_area.append(val)
        else:
            val = max_area[i]
            m_area.append(val)
    #convert to float
    m_area = [float(i) for i in m_area]

    #make sure lenght is the same
    if len(m_area) != len(ser_per):
        return
    #total area
    total_area = []
    for i in np.arange(0,len(ser_per)):
        val = (ser_per[i]/100) * m_area[i]
        total_area.append(val)

    print("Total High Elevation Grasslands: %s ha" % round(sum(total_area),2))

    #sum areas for specified polygons
    if len(Polygons) >= 1:
        new_sum = []
        vals_table = []
        for i in Polygon:
            try:
                ind = np.where(fes["Shape ID"].reset_index() == i)[0][0]
                new_sum.append(total_area[ind])
                vals_table.append((i,round(total_area[ind],2)))
            except:
                pass
    #print results
    print("Total: %s ha" % round(sum(new_sum),2))
    return vals_table



Polygon = [121698,121699,121695,121794,121696,121700,121702]
fesc_c = "Festuca campestris"
fesc_i = "Festuca idahoensis"

#Function at work
return_area(SER,fesc_c,Polygon)
