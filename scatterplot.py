import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt


games = pd.read_excel("ALL_DATA.xlsx", sheet_name="ALL DATA")

jl = []
margins = []

for r in range(len(games)):
    if games.iloc[r][9] > -1000 and games.iloc[r][9] < 1000 and games.iloc[r][10] > -1000 and games.iloc[r][10] < 1000:
        if games.iloc[r][11] < 10 and games.iloc[r][11] > -10:
            jl.append(games.iloc[r][10])
            margins.append(games.iloc[r][11])
            jl.append(games.iloc[r][9])
            margins.append(-1*games.iloc[r][11])

plt.scatter(jl, margins, s=4)
plt.yscale('log')
plt.xscale('log')
#plt.loglog(jl, margins)
plt.xlabel("Jet Lag Value")
plt.ylabel("Win/loss Margin")
plt.show()