import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import statistics

games = pd.read_excel("ALL_DATA.xlsx", sheet_name="ALL DATA")

no_lag_runs_scored = []
lag_runs_scored = []
no_lag_runs_allowed = []
lag_runs_allowed = []

for r in range(len(games)):

    #away no JL
    if games.iloc[r][9] == 0:
        no_lag_runs_scored.append(games.iloc[r][6])
        no_lag_runs_allowed.append(games.iloc[r][7])
    #home no JL
    if games.iloc[r][10] == 0:
        no_lag_runs_scored.append(games.iloc[r][7])
        no_lag_runs_allowed.append(games.iloc[r][6])
    #away yes JL
    if games.iloc[r][9] != 0:
        lag_runs_scored.append(games.iloc[r][6])
        lag_runs_allowed.append(games.iloc[r][7])
    #home yes JL
    if games.iloc[r][10] != 0:
        lag_runs_scored.append(games.iloc[r][7])
        lag_runs_allowed.append(games.iloc[r][6])


print(len(lag_runs_allowed))
print(len(lag_runs_scored))


print("No lag runs scored avg:", statistics.mean(no_lag_runs_scored))
print()
print("Lag runs scored avg:", statistics.mean(lag_runs_scored))
print()
print("No lag runs allowed avg:", statistics.mean(no_lag_runs_allowed))
print()
print("Lag runs allowed avg:", statistics.mean(lag_runs_allowed))
print()

print("No lag runs scored SD:", statistics.stdev(no_lag_runs_scored))
print()
print("Lag runs scored SD:", statistics.stdev(lag_runs_scored))
print()
print("No lag runs allowed SD:", statistics.stdev(no_lag_runs_allowed))
print()
print("Lag runs allowed SD:", statistics.stdev(lag_runs_allowed))
print()