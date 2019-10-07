#This file contains necessary code to acquire salary cap data from sportrac.com and generate a dataframe

import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup


teams = ["arizona-cardinals","atlanta-falcons","baltimore-ravens","buffalo-bills","carolina-panthers","chicago-bears","cincinnati-bengals","cleveland-browns","dallas-cowboys","denver-broncos","detroit-lions","green-bay-packers","houston-texans","indianapolis-colts","jacksonville-jaguars","kansas-city-chiefs","los-angeles-chargers","los-angeles-rams","miami-dolphins","minnesota-vikings","new-england-patriots","new-orleans-saints","new-york-giants","new-york-jets","oakland-raiders","philadelphia-eagles","pittsburgh-steelers","san-francisco-49ers","seattle-seahawks","tampa-bay-buccaneers","tennessee-titans","washington-redskins"]

years = ["2013","2014","2015","2016","2017","2018","2019"]

def get_team_cap_info(team,year,session):
    url = "https://www.spotrac.com/nfl/{}/positional/{}/full-cap/".format(team,year)

    response = session.get(url)


    page = response.text

    soup = BeautifulSoup(page,"lxml")
    active_contracts_block = soup.find(string="Active Contracts:")

    #let's go looking for the value!
    active_contracts_text = active_contracts_block.parent.parent.next_sibling.next_sibling.contents

    active_contracts_value = int(active_contracts_text[0].replace("$","").replace(",",""))

    dead_cap_block = soup.find(string="Dead Cap:")
    dead_cap_text = dead_cap_block.parent.parent.next_sibling.next_sibling.contents[0]

    dead_cap_value = int(dead_cap_text.replace("$","").replace(",",""))

    injured_reserve_block = soup.find(string="Injured Reserve:")
    injured_reserve_text = injured_reserve_block.parent.parent.next_sibling.next_sibling.contents[0]

    injured_reserve_value = int(injured_reserve_text.replace("$","").replace(",",""))

    #build a dataframe from a dict and return it
    dict = {"Team":[team],"Year":[year],"Active Contracts":[active_contracts_value],"Dead Cap":[dead_cap_value],"Injured Reserve":[injured_reserve_value]}

    return pd.DataFrame.from_dict(dict)

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount("http://", adapter)
session.mount("https://", adapter)

active_contracts_frame = pd.concat([get_team_cap_info(team, year, session) for team in teams for year in years])

active_contracts_frame.to_csv("../data/active_contract_dead_cap_data.csv",index=False)

