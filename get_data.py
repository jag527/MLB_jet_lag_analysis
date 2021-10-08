# to return an array consisting of complete game schedule
# (and results) from _____ MLB season.

from ohmysportsfeedspy import MySportsFeeds

import pandas as pd
import numpy as np

# create feed
msf = MySportsFeeds(version='2.0')
msf.authenticate('060c60b4-c81a-40a0-a063-097427', 'MYSPORTSFEEDS')
output = msf.msf_get_data(league='mlb',season='2019-2020-regular',feed='seasonal_games',format='csv')

# convert feed to DataFrame df
df = pd.DataFrame(output)

# assign column names as each header in DataFrame
column_names = str(df.loc[0][0]).split(",")

# create second DataFrame using column_names as the columns
df2 = pd.DataFrame(columns = column_names)

# transfer data from df to df2
for i in range(1, len(df)):
    array = str(df.loc[i][0]).split(",")
    row = dict(zip(column_names, array))
    
    df2 = df2.append(row, ignore_index = True)

# remove 51 of the 59 columns – keep necessary ones
df2 = df2.loc[:, [" '#Game Date'", " '#Game Time'", " '#Away Team Abbr.'", " '#Away Team Name'",
 " '#Home Team Abbr.'", " '#Home Team Name'", " '#Away Score Total'", " '#Home Score Total'"]]

# goes item by item in entire spreadsheet, removes extra quotation marks and space
# converts string numerical values into usable ints
for r in range(len(df2)):
    for c in range(8):
        df2.loc[r][c] = df2.loc[r][c][2:(len(df2.loc[r][c])-1)]

# convert DataFrame to .csv file
df2.to_csv("2019_data2.csv")