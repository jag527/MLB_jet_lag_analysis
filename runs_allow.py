import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

data = pd.read_excel("ALL_DATA.xlsx", sheet_name="ALL DATA")


teams = ["ATL", "MIA", "NYM", "PHI", "WAS",
"CHC", "CIN", "MIL", "PIT", "STL",
"ARI", "COL", "LAD", "SD", "SF",
"BAL", "BOS", "NYY", "TB", "TOR",
"CWS", "CLE", "DET", "KC", "MIN",
"HOU", "LAA", "OAK", "SEA", "TEX"]



def no_lag(team):
    total_games = 0
    total_runs_allowed = 0
    rapg = 0
    for r in range(len(data)):
        # away
        if data.iloc[r][2] == team and data.iloc[r][9] == 0:
            total_runs_allowed += data.iloc[r][7]
            total_games += 1
            
        # home
        elif data.iloc[r][4] == team and data.iloc[r][10] == 0:
            total_runs_allowed += data.iloc[r][6]
            total_games += 1
    
    rapg = total_runs_allowed/total_games

    print(team)
    print("NO LAG Games: ", total_games)
    print("NO LAG runs allowed: ", total_runs_allowed)
    print("NO LAG rapg: ", rapg)
    print()


def lag(team):
    total_games = 0
    total_runs_allowed = 0
    rapg = 0
    for r in range(len(data)):
        # away
        if data.iloc[r][2] == team and data.iloc[r][9] != 0:
            total_runs_allowed += data.iloc[r][7]
            total_games += 1
            
        # home
        elif data.iloc[r][4] == team and data.iloc[r][10] != 0:
            total_runs_allowed += data.iloc[r][6]
            total_games += 1
    
    rapg = total_runs_allowed/total_games

    print(team)
    print("LAG Games: ", total_games)
    print("LAG runs allowed: ", total_runs_allowed)
    print("LAG rapg: ", rapg)
    print()




for t in teams:
    no_lag(t)
    lag(t)