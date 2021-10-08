import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import statistics

data = pd.read_excel("ALL_DATA.xlsx", sheet_name="ALL DATA")

east = []
west = []

#for r in range(len(data)):
    #if data.iloc[r][9] > 0:
       # east.append(data.iloc[r][6])
    #if data.iloc[r][9] < 0:
    #    west.append(data.iloc[r][6])
    #if data.iloc[r][10] > 0:
   #     east.append(data.iloc[r][7])
    #if data.iloc[r][10] < 0:
    #    west.append(data.iloc[r][7])

#east_sd = statistics.stdev(east)
#west_sd = statistics.stdev(west)

#print("east lag r/g std. dev:", east_sd)
#print("west lag r/g std. dev:", west_sd)



for r in range(len(data)):
    if data.iloc[r][9] > 0:
        east.append(data.iloc[r][7])
    if data.iloc[r][9] < 0:
        west.append(data.iloc[r][7])
    if data.iloc[r][10] > 0:
        east.append(data.iloc[r][6])
    if data.iloc[r][10] < 0:
        west.append(data.iloc[r][6])

east_sd = statistics.stdev(east)
west_sd = statistics.stdev(west)

print("east lag ra/g std. dev:", east_sd)
print("west lag ra/g std. dev:", west_sd)

