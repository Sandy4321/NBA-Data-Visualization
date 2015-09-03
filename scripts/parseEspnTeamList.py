import pandas as pd
import requests
from bs4 import BeautifulSoup

# Valid sports: nba, nfl, nhl, mlb
sport = 'nba'
url = 'http://espn.go.com/' + sport + '/teams'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
tables = soup.find_all('ul', class_='medium-logos')