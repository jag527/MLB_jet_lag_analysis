import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import statistics

data = pd.read_excel("ALL_DATA.xlsx", sheet_name="ALL DATA")

extreme_lag = []
mod_lag = []

extreme_lag_ra = []
mod_lag_ra = []

for r in range(len(data)):
    if data.iloc[r][9] < -500 or data.iloc[r][9] > 500:
        extreme_lag.append(data.iloc[r][6])
    if data.iloc[r][10] < -500 or data.iloc[r][10] > 500:
        extreme_lag.append(data.iloc[r][7])
    if (data.iloc[r][9] > -500 and data.iloc[r][9] < 0) or (data.iloc[r][9] < 500 and data.iloc[r][9] > 0):
        mod_lag.append(data.iloc[r][6])
    if (data.iloc[r][10] > -500 and data.iloc[r][10] < 0) or (data.iloc[r][10] < 500 and data.iloc[r][10] > 0):
        mod_lag.append(data.iloc[r][7])

    if data.iloc[r][9] < -500 or data.iloc[r][9] > 500:
        extreme_lag_ra.append(data.iloc[r][7])
    if data.iloc[r][10] < -500 or data.iloc[r][10] > 500:
        extreme_lag_ra.append(data.iloc[r][6])
    if (data.iloc[r][9] > -500 and data.iloc[r][9] < 0) or (data.iloc[r][9] < 500 and data.iloc[r][9] > 0):
        mod_lag_ra.append(data.iloc[r][7])
    if (data.iloc[r][10] > -500 and data.iloc[r][10] < 0) or (data.iloc[r][10] < 500 and data.iloc[r][10] > 0):
        mod_lag_ra.append(data.iloc[r][6])


print("extreme_lag avg. r/g:", statistics.mean(extreme_lag))
print("mod_lag avg. r/g:", statistics.mean(mod_lag))
print("extreme_lag SD:", statistics.stdev(extreme_lag))
print("mod_lag SD:", statistics.stdev(mod_lag))
print()
print("extreme_lag_ra avg. ra/g:", statistics.mean(extreme_lag_ra))
print("mod_lag_ra avg. ra/g:", statistics.mean(mod_lag_ra))
print("extreme_lag_ra SD:", statistics.stdev(extreme_lag_ra))
print("mod_lag_ra SD:", statistics.stdev(mod_lag_ra))