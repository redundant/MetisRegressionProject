import pandas as pd

years = [2013,2014,2015,2016,2017,2018]

def get_year_win_data(year):
    """This takes in an integer year and returns a dataset with wins for each nfl team. Data scraped off of wikipedia."""

    url = "https://en.wikipedia.org/wiki/{}_NFL_season".format(year)
    data = pd.read_html(url)[2]


    data = data.rename(columns = {0:"Team",1:"Wins"})

    #remove
    filter1 = ~ data["Team"].str.contains(".FC",regex=True)
    filter2 = ~ data["Team"].str.contains("viewtalk",regex=False)

    data = data[filter1 & filter2]
    data["Year"] = year
    return data[["Year","Team","Wins"]]


wins = pd.concat([get_year_win_data(year) for year in years])
wins.to_csv("wins.csv")
