#This file contains necessary code to acquire salary data from sportrac.com and generate a dataframe

import pandas as pd

teams = ["arizona-cardinals","atlanta-falcons","baltimore-ravens","buffalo-bills","carolina-panthers","chicago-bears","cincinnati-bengals","cleveland-browns","dallas-cowboys","denver-broncos","detroit-lions","green-bay-packers","houston-texans","indianapolis-colts","jacksonville-jaguars","kansas-city-chiefs","los-angeles-chargers","los-angeles-rams","miami-dolphins","minnesota-vikings","new-england-patriots","new-orleans-saints","new-york-giants","new-york-jets","oakland-raiders","philadelphia-eagles","pittsburgh-steelers","san-francisco-49ers","seattle-seahawks","tampa-bay-buccaneers","tennessee-titans","washington-redskins"]

years = ["2013","2014","2015","2016","2017","2018","2019"]

def get_team_year_data(team,year):
    """Given a team and year, scrapes from sportrac and returns a nice, flattened dataframe"""

    url = "https://www.spotrac.com/nfl/{}/positional/{}/active-cap/"

    data = pd.read_html(url.format(team,year))[1]
    data["Team"] = team
    data["Cap Dollars"] = data["Cap Dollars"].apply(lambda x: int(x[1:].replace(",","")))
    data = data.pivot(index="Team", columns="Position", values="Cap Dollars")
    data["Year"] = int(year)

    #The pivot removed the team column, so let's throw it back in
    data["Team"] = team

    return data

nfl_data = pd.concat([get_team_year_data(team,year) for team in teams for year in years])
nfl_data.to_csv("../data/salary_data.csv",index=False)
