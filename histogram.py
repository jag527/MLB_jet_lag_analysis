import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import statistics

games = pd.read_excel("ALL_DATA.xlsx", sheet_name="ALL DATA")

neglessthan750 = []
neg750to500 = []
neg500to250 = []
neg250tozero = []
zero = []
zeroto250 = []
plus250to500 = []
plus500to750 = []
plus750bigger = []

pointless = 0


# each game
for r in range(len(games)):


#games.iloc[r][9] (home)
#games.iloc[r][10] (away, make sure to multiply by -1)


    #home win
    if games.iloc[r][9] < -1000:
        pointless += 1
    elif games.iloc[r][9] < -750 and games.iloc[r][9] >= -1000:
        neglessthan750.append(games.iloc[r][11])
    elif games.iloc[r][9] < -500:
        neg750to500.append(games.iloc[r][11])
    elif games.iloc[r][9] < -250:
        neg500to250.append(games.iloc[r][11])
    elif games.iloc[r][9] < 0:
        neg250tozero.append(games.iloc[r][11])
    elif games.iloc[r][9] == 0:
        zero.append(games.iloc[r][11])
    elif games.iloc[r][9] < 250:
        zeroto250.append(games.iloc[r][11])
    elif games.iloc[r][9] < 500:
        plus250to500.append(games.iloc[r][11])
    elif games.iloc[r][9] < 750:
        plus500to750.append(games.iloc[r][11])
    elif games.iloc[r][9] >= 750 and games.iloc[r][9] <= 1000:
        plus750bigger.append(games.iloc[r][11])

    if games.iloc[r][10] < -1000:
        pointless += 1
    elif games.iloc[r][10] < -750 and games.iloc[r][10] >= -1000:
        neglessthan750.append(-1*(games.iloc[r][11]))
    elif games.iloc[r][10] < -500:
        neg750to500.append(-1*(games.iloc[r][11]))
    elif games.iloc[r][10] < -250:
        neg500to250.append(-1*(games.iloc[r][11]))
    elif games.iloc[r][10] < 0:
        neg250tozero.append(-1*(games.iloc[r][11]))
    elif games.iloc[r][10] == 0:
        zero.append(-1*(games.iloc[r][11]))
    elif games.iloc[r][10] < 250:
        zeroto250.append(-1*(games.iloc[r][11]))
    elif games.iloc[r][10] < 500:
        plus250to500.append(-1*(games.iloc[r][11]))
    elif games.iloc[r][10] < 750:
        plus500to750.append(-1*(games.iloc[r][11]))
    elif games.iloc[r][10] >= 750 and games.iloc[r][10] <= 1000:
        plus750bigger.append(-1*(games.iloc[r][11]))









print("neglessthan750 mean win margin:", statistics.mean(neglessthan750), "n:", len(neglessthan750), "std dev:", statistics.stdev(neglessthan750))
print()
print("neg750to500 mean win margin:", statistics.mean(neg750to500), "n:", len(neg750to500), "std dev:", statistics.stdev(neg750to500))
print()
print("neg500to250 mean win margin:", statistics.mean(neg500to250), "n:", len(neg500to250), "std dev:", statistics.stdev(neg500to250))
print()
print("neg250tozero mean win margin:", statistics.mean(neg250tozero), "n:", len(neg250tozero), "std dev:", statistics.stdev(neg250tozero))
print()
print("zero mean win margin:", statistics.mean(zero), "n:", len(zero), "std dev:", statistics.stdev(zero))
print()
print("zeroto250 mean win margin:", statistics.mean(zeroto250), "n:", len(zeroto250), "std dev:", statistics.stdev(zeroto250))
print()
print("plus250to500 mean win margin:", statistics.mean(plus250to500), "n:", len(plus250to500), "std dev:", statistics.stdev(plus250to500))
print()
print("plus500to750 mean win margin:", statistics.mean(plus500to750), "n:", len(plus500to750), "std dev:", statistics.stdev(plus500to750))
print()
print("plus750bigger mean win margin:", statistics.mean(plus750bigger), "n:", len(plus750bigger), "std dev:", statistics.stdev(plus750bigger))
print()


print("total games:", (len(neglessthan750) + len(neg750to500) + len(neg500to250) + len(neg250tozero) + len(zero) + len(zeroto250) + len(plus250to500) + len(plus500to750) + len(plus750bigger)))