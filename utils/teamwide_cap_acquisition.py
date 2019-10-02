#This file contains necessary code to acquire salary cap data from sportrac.com and generate a dataframe

import pandas as pd
import requests
from bs4 import BeautifulSoup

teams = ["arizona-cardinals","atlanta-falcons","baltimore-ravens","buffalo-bills","carolina-panthers","chicago-bears","cincinnati-bengals","cleveland-browns","dallas-cowboys","denver-broncos","detroit-lions","green-bay-packers","houston-texans","indianapolis-colts","jacksonville-jaguars","kansas-city-chiefs","los-angeles-chargers","los-angeles-rams","miami-dolphins","minnesota-vikings","new-england-patriots","new-orleans-saints","new-york-giants","new-york-jets","oakland-raiders","philadelphia-eagles","pittsburgh-steelers","san-francisco-49ers","seattle-seahawks","tampa-bay-buccaneers","tennessee-titans","washington-redskins"]

years = ["2013","2014","2015","2016","2017","2018","2019"]

def get_team_cap_info(team,year):
    url = "https://www.spotrac.com/nfl/{}/positional/{}/full-cap/".format(team,year)

    response = requests.get(url)
    page = response.text

    soup = BeautifulSoup(page,"lxml")
    active_contracts_block = soup.find(string="Active Contracts:")

    #let's go looking for the value!
    active_contracts_text = active_contracts_block.parent.parent.next_sibling.next_sibling.contents

    active_contracts_value = int(active_contracts_text[0].replace("$","").replace(",",""))

    #build a dataframe from a dict and return it
    dict = {"Team":[team],"Year":[year],"Active Contracts":[active_contracts_value]}

    return pd.DataFrame.from_dict(dict)

active_contracts_frame = pd.concat([get_team_cap_info(team,year) for team in teams for year in years])

active_contracts_frame.to_csv("../active_contract_data.csv",index=False)

