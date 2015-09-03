import pandas as pd
import requests
from bs4 import BeautifulSoup

# Valid sports: nba, nfl, nhl, mlb
sport = 'nba'
url = 'http://espn.go.com/' + sport + '/teams'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
tables = soup.find_all('ul', class_='medium-logos')

teams = []
abbreviations = []
urls = []

for table in tables:
    teamList = table.find_all('li')
    for li in teamList:
        # extract team urls
        info = li.h5.a
        # isolate team name from urls
        teams.append(info.text)
        url = info['href']
        urls.append(url)
        abbreviations.append(url.split('/')[-2])

columns = {'abbreviations': abbreviations}
teams = pd.DataFrame(columns, index=teams)
teams.index.name = 'team'
print(teams)
