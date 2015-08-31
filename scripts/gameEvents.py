import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from IPython.display import display

def functionname(player_id):
  shot_chart_url =  'http://stats.nba.com/stats/shotchartdetail?CFID=33'\
                      '&CFPARAMS=2014-15'\
                      '&ContextFilter='\
                      '&ContextMeasure=FGA'\
                      '&DateFrom='\
                      '&DateTo='\
                      '&GameID='\
                      '&GameSegment='\
                      '&LastNGames=0'\
                      '&LeagueID=00'\
                      '&Location='\
                      '&MeasureType=Base'\
                      '&Month=0'\
                      '&OpponentTeamID=0'\
                      '&Outcome='\
                      '&PaceAdjust=N'\
                      '&PerMode=PerGame'\
                      '&Period=0'\
                      '&PlayerID='+player_id+\
                      '&PlusMinus=N'\
                      '&Position='\
                      '&Rank=N'\
                      '&RookieYear='\
                      '&Season=2014-15'\
                      '&SeasonSegment='\
                      '&SeasonType=Regular+Season'\
                      '&TeamID=0'\
                      '&VsConference='\
                      '&VsDivision='\
                      '&mode=Advanced'\
                      '&showDetails=0'\
                      '&showShots=1'\
                      '&showZones=0'

  response = requests.get(shot_chart_url)
  headers = response.json()['resultSets'][0]['headers']
  shots = response.json()['resultSets'][0]['rowSet']
  shot_df = pd.DataFrame(shots, columns=headers)
  with pd.option_context('display.max_columns', None):
      display(shot_df.head())

def main():
  functionname(101108) # Player ID for Chris Paul