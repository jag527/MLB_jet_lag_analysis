import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import math
from math import cos, asin, sqrt
import datetime
from datetime import datetime


yearstats = pd.read_excel("2019_data.xlsx", sheet_name="2019_data")
locations = pd.read_excel("2019_data.xlsx", sheet_name="Team Locations")
team_stats = pd.read_excel("2019_data.xlsx", sheet_name="2019 Team Stats")


teams = ["ATL", "MIA", "NYM", "PHI", "WAS",
"CHC", "CIN", "MIL", "PIT", "STL",
"ARI", "COL", "LAD", "SD", "SF",
"BAL", "BOS", "NYY", "TB", "TOR",
"CWS", "CLE", "DET", "KC", "MIN",
"HOU", "LAA", "OAK", "SEA", "TEX"]



# array of arrays 
# each array within has the distance travelled for every team, each index is distance from past game to present
all_teams_distances = []
all_teams_deltazone = []
all_teams_westeast = []
all_teams_time_btw_games = []
all_teams_jet_lag = []


# returns distance between two sets of latitudes and longitude points in miles
def distance_travelled(latitude_away, longitude_away, latitude_home, longitude_home):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((latitude_home - latitude_away) * p)/2 + cos(latitude_away * p) * cos(latitude_home * p) * (1 - cos((longitude_home - longitude_away) * p)) / 2
    return 7918 * asin(sqrt(a)) #2*R*asin...



# calculates hours between current and previous game start
def calc_time_btw_games(date_curr, date_prev, time_curr, time_prev):
    date_format = "%m-%d-%Y %H:%M:%S"
    time1 = datetime.strptime(date_prev + " " + time_prev, date_format)
    time2 = datetime.strptime(date_curr + " " + time_curr, date_format)

    diff = time2 - time1
    days = diff.days
    days_to_hours = days*24
    diff_btw_two_times = (diff.seconds)/3600
    overall_hours = days_to_hours + diff_btw_two_times
    return overall_hours



# returns value of jet lag following equation: jetlag = (Delta miles * abs(delta time))/time btw games)
def calc_jetlag(change_miles, change_zones, change_time):
    return ((change_miles * change_zones)/change_time)



def edit_sheet(jlag, row, isaway):
    if (isaway == True):
        yearstats.at[row, "Away Calculated JL"] = jlag
    if (isaway == False):
        yearstats.at[row, "Home Calculated JL"] = jlag



# loop over each team in list of all teams
for team in teams:
    # first_game ensures that I don't try calculating 
    # distance travelled from a game before a team's first game
    first_game = True

    team_distances = []
    team_deltazone = []
    team_westeast = []
    team_time_btw_games = []
    # time btw games given in hours

    team_jet_lag = []

    game = 0

    # go row by row
    for r in range(len(yearstats)):

        # if game is the team's first game of season
        if ((yearstats.iloc[r][2] == team or yearstats.iloc[r][4] == team)) and (first_game == True):
            first_game = False

            team_distances.append(0.0)
            team_deltazone.append(0)
            team_westeast.append("n/a")
            team_time_btw_games.append(0.0)
            team_jet_lag.append(0.0)

            # edit jet_lag_results sheet with proper jet lag calculation for this specific game
            if (yearstats.iloc[r][2] == team):
                edit_sheet(0.0, r, True)
            else:
                edit_sheet(0.0, r, False)

            game += 1

            yearstats.at[r, "Win Margin – positive means home wins, negative away"] = (int(yearstats.iloc[r][7]) - int(yearstats.iloc[r][6]))


        # if team played in game, not first game of season
        elif ((yearstats.iloc[r][2] == team or yearstats.iloc[r][4] == team) and (first_game == False)):
            dist = 0.0
            zone = 0

            current_home_team = yearstats.iloc[r][4]

            # finds home team of team's previous game
            i = r - 1
            while yearstats.iloc[i][2] != team and yearstats.iloc[i][4] != team:
                i -= 1
            
            prev_home_team = yearstats.iloc[i][4]

            #get current game's date, replace "/"s with "-"s 
            current_date = str(yearstats.iloc[r][0])[0:10]
            current_date = str(current_date).replace("/", "-")
            current_date = current_date[5:8] + current_date[8:10] + "-" + current_date[0:4]

            # get current game's time, remove "GMT"
            current_time = yearstats.iloc[r][1][0:8]


            #get prev game's date, replace "/"s with "-"s 
            prev_date = str(yearstats.iloc[i][0])[0:10]
            prev_date = str(prev_date).replace("/", "-")
            prev_date = prev_date[5:8] + prev_date[8:10] + "-" + prev_date[0:4]

            # get prev game's time, remove "GMT"
            prev_time = yearstats.iloc[i][1][0:8]


            chg_time = calc_time_btw_games(current_date, prev_date, current_time, prev_time)
            team_time_btw_games.append(chg_time)


            lat_current = 0.0
            lon_current = 0.0

            lat_prev = 0.0
            lon_prev = 0.0

            # find lat and lon of current, prev home team
            # calculate how many time zones switched (+ or -)
            for x in range(len(locations)):
                if (locations.iloc[x][0] == current_home_team):
                    lat_current = locations.iloc[x][1]
                    lon_current = locations.iloc[x][2]

                    zone += locations.iloc[x][3]
                    

                if (locations.iloc[x][0] == prev_home_team):
                    lat_prev = locations.iloc[x][1]
                    lon_prev = locations.iloc[x][2]

                    zone -= locations.iloc[x][3]

            # calculate distance from prev to current home
            # add to list 
            # add amount of timezones changed to list
            # determine if jet lag is east, west, or none
            dist = distance_travelled(lat_current, lon_current, lat_prev, lon_prev)
            team_distances.append(dist)
            team_deltazone.append(zone)
            if (zone > 0):
                team_westeast.append("EAST")
            if (zone < 0):
                team_westeast.append("WEST")
            if (zone == 0):
                team_westeast.append("n/a")

            lag = calc_jetlag(dist, zone, chg_time)
            team_jet_lag.append(lag)


            # edit jet_lag_results sheet with proper jet lag calculation for this specific game
            if (yearstats.iloc[r][2] == team):
                edit_sheet(lag, r, True)
            else:
                edit_sheet(lag, r, False)


            game += 1


            yearstats.at[r, "Win Margin – positive means home wins, negative away"] = (int(yearstats.iloc[r][7]) - int(yearstats.iloc[r][6]))



    print()
    print(team + " calculated jet lag:")
    print(team_jet_lag)
    print()

    # add each list to list
    all_teams_distances.append(team_distances)
    all_teams_deltazone.append(team_deltazone)
    all_teams_westeast.append(team_westeast)
    all_teams_time_btw_games.append(team_time_btw_games)


yearstats.to_excel("2019_JETLAG_RESULTS.xlsx")



