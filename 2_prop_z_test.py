import math
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

data = pd.read_excel("ALL_DATA.xlsx", sheet_name="Final Stats")


teams = ["ATL", "MIA", "NYM", "PHI", "WAS",
"CHC", "CIN", "MIL", "PIT", "STL",
"ARI", "COL", "LAD", "SD", "SF",
"BAL", "BOS", "NYY", "TB", "TOR",
"CWS", "CLE", "DET", "KC", "MIN",
"HOU", "LAA", "OAK", "SEA", "TEX"]

def test(value1, n1, value2, n2):
    ppool = ((value1+value2)/(n1+n2))
    qpool = 1 - ppool
    p1 = value1/n1
    p2 = value2/n2

    z = (p1 - p2)/(math.sqrt(((ppool*qpool)/n1) + ((ppool*qpool)/n2)))

    return z


r = 0
for t in teams:
    no_lag_games = data.iloc[r][12]
    no_lag_wins = data.iloc[r][13]
    lag_games = data.iloc[r][14]
    lag_wins = data.iloc[r][15]
    z_score = test(no_lag_wins, no_lag_games, lag_wins, lag_games)
    print(t)
    print("Z-score:", z_score)
    print()
    r += 1

