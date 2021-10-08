import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import statistics

data = pd.read_excel("ALL_DATA.xlsx", sheet_name="ALL DATA")


teams = ["ATL", "MIA", "NYM", "PHI", "WAS",
"CHC", "CIN", "MIL", "PIT", "STL",
"ARI", "COL", "LAD", "SD", "SF",
"BAL", "BOS", "NYY", "TB", "TOR",
"CWS", "CLE", "DET", "KC", "MIN",
"HOU", "LAA", "OAK", "SEA", "TEX"]

no_lag_runs_scored = []
lag_runs_scored = []
no_lag_runs_allowed = []
lag_runs_allowed = []


def no_lag(team):
    #total_games = 0
    #total_runs = 0
    #rpg = 0
    for r in range(len(data)):
        # away
        if data.iloc[r][2] == team and data.iloc[r][9] == 0:
            #total_runs += data.iloc[r][6]
            no_lag_runs_scored.append(data.iloc[r][6])
            no_lag_runs_allowed.append(data.iloc[r][7])
            #total_games += 1
            
        # home
        elif data.iloc[r][4] == team and data.iloc[r][10] == 0:
            #total_runs += data.iloc[r][7]
            no_lag_runs_scored.append(data.iloc[r][7])
            no_lag_runs_allowed.append(data.iloc[r][6])
            #total_games += 1

    #rpg = total_runs/total_games

    #print(team)
    #print("NO LAG Games: ", total_games)
    #print("NO LAG runs: ", total_runs)
    #print("NO LAG rpg: ", rpg)
    #print()


def lag(team):
    #total_games = 0
    #total_runs = 0
    #rpg = 0
    for r in range(len(data)):
        # away
        if data.iloc[r][2] == team and data.iloc[r][9] != 0:
            #total_runs += data.iloc[r][6]
            lag_runs_scored.append(data.iloc[r][6])
            lag_runs_allowed.append(data.iloc[r][7])
            #total_games += 1
            
        # home
        elif data.iloc[r][4] == team and data.iloc[r][10] != 0:
            #total_runs += data.iloc[r][7]
            lag_runs_scored.append(data.iloc[r][7])
            lag_runs_allowed.append(data.iloc[r][6])
            #total_games += 1

    #rpg = total_runs/total_games

    #print(team)
    #print("LAG Games: ", total_games)
    #print("LAG runs: ", total_runs)
    #print("LAG rpg: ", rpg)
    #print()

for t in teams:
    no_lag(t)
    lag(t)

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