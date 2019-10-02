# this provides a function to import that takes a scraped dataframe and changes the names to match with the main dataset

import pandas as pd

def rename_nfl_teams(df):
    """Takes in a pandas dataframe scaped from spotrac and changes the names to human readable

    For example, "carolina-panthers" becomes "Carolina Panthers". Furthermore team moves are suppressed. That is, the Rams/Chargers have always been in LA"""

    d = {"arizona-cardinals":"Arizona Cardinals","atlanta-falcons":"Atlanta Falcons","baltimore-ravens":"Baltimore Ravens","buffalo-bills":"Buffalo Bills", "carolina-panthers":"Carolina Panthers","chicago-bears":"Chicago Bears","cincinnati-bengals":"Cincinnati Bengals","cleveland-browns":"Cleveland Browns","dallas-cowboys":"Dallas Cowboys","denver-broncos":"Denver Broncos","detroit-lions":"Detroit Lions","green-bay-packers":"Green Bay Packers","houston-texans":"Houston Texans","indianapolis-colts":"Indianapolis Colts","jacksonville-jaguars":"Jacksonville Jaguars","kansas-city-chiefs":"Kansas City Chiefs","los-angeles-chargers":"Los Angeles Chargers","los-angeles-rams":"Los Angeles Rams","miami-dolphins":"Miami Dolphins","minnesota-vikings":"Minnesota Vikings","new-england-patriots":"New England Patriots","new-orleans-saints":"New Orleans Saints","new-york-giants":"New York Giants","new-york-jets":"New York Jets","oakland-raiders":"Oakland Raiders","philadelphia-eagles":"Philadelphia Eagles","pittsburgh-steelers":"Pittsburgh Steelers","san-francisco-49ers":"San Francisco 49ers","seattle-seahawks":"Seattle Seahawks","tampa-bay-buccaneers":"Tampa Bay Buccaneers","tennessee-titans":"Tennessee Titans","washington-redskins":"Washington Redskins"}

    return df["Team"].map(d)
