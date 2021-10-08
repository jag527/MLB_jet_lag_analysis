import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

yearstats = pd.read_excel("2016_data.xlsx", sheet_name="2016_data")
team_stats = pd.read_excel("2016_data.xlsx", sheet_name="2016 Team Stats")


teams = ["ATL", "MIA", "NYM", "PHI", "WAS",
"CHC", "CIN", "MIL", "PIT", "STL",
"ARI", "COL", "LAD", "SD", "SF",
"BAL", "BOS", "NYY", "TB", "TOR",
"CWS", "CLE", "DET", "KC", "MIN",
"HOU", "LAA", "OAK", "SEA", "TEX"]



def no_lag(team):
    games = 0
    wins = 0
    win_percent = 0
    for r in range(len(yearstats)):
        # away
        if yearstats.iloc[r][2] == team and yearstats.iloc[r][9] == 0:
            # win
            if yearstats.iloc[r][11] < 0:
                games += 1
                wins += 1
            # loss
            elif yearstats.iloc[r][11] > 0:
                games += 1
            
        # home
        elif yearstats.iloc[r][4] == team and yearstats.iloc[r][10] == 0:
            # win
            if yearstats.iloc[r][11] > 0:
                games += 1
                wins += 1
            # loss
            elif yearstats.iloc[r][11] < 0:
                games += 1
    
    win_percent = wins/games

    print(team)
    print("NO LAG Games: ", games)
    print("NO LAG Wins: ", wins)
    print("NO LAG Win percent: ", win_percent)
    print()


def west_lag(team):
    games = 0
    wins = 0
    win_percent = 0
    for r in range(len(yearstats)):
        # away, west lag
        if yearstats.iloc[r][2] == team and yearstats.iloc[r][9] > 0:
            # win
            if yearstats.iloc[r][11] < 0:
                games += 1
                wins += 1
            # loss
            elif yearstats.iloc[r][11] > 0:
                games += 1
            
        # home, west lag
        elif yearstats.iloc[r][4] == team and yearstats.iloc[r][10] > 0:
            # win
            if yearstats.iloc[r][11] > 0:
                games += 1
                wins += 1
            # loss
            elif yearstats.iloc[r][11] < 0:
                games += 1
    
    win_percent = wins/games

    print(team)
    print("WEST LAG Games: ", games)
    print("WEST LAG Wins: ", wins)
    print("WEST LAG Win percent: ", win_percent)
    print()


def east_lag(team):
    games = 0
    wins = 0
    win_percent = 0
    for r in range(len(yearstats)):
        # away, west lag
        if yearstats.iloc[r][2] == team and yearstats.iloc[r][9] < 0:
            # win
            if yearstats.iloc[r][11] < 0:
                games += 1
                wins += 1
            # loss
            elif yearstats.iloc[r][11] > 0:
                games += 1
            
        # home, west lag
        elif yearstats.iloc[r][4] == team and yearstats.iloc[r][10] < 0:
            # win
            if yearstats.iloc[r][11] > 0:
                games += 1
                wins += 1
            # loss
            elif yearstats.iloc[r][11] < 0:
                games += 1
    
    win_percent = wins/games

    print(team)
    print("EAST LAG Games: ", games)
    print("EAST LAG Wins: ", wins)
    print("EAST LAG Win percent: ", win_percent)
    print()



for t in teams:
    #no_lag(t)
    #west_lag(t)
    #east_lag(t)
    
