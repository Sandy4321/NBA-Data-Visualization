import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
from matplotlib.patches import Circle, Rectangle, Arc

shot_chart = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPARAMS=2014'\
             '-15&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&GameID=&'\
             'GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base'\
             '&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&'\
             'Period=0&PlayerID=101108&PlusMinus=N&Position=&Rank=N&RookieYear'\
             '=&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID'\
             '=0&VsConference=&VsDivision=&mode=Advanced&showDetails=0&showSho'\
             'ts=1&showZones=0'

response = requests.get(shot_chart)
headers = response.json()['resultSets'][0]['headers']
# Grab shot chart data
shots = response.json()['resultSets'][0]['rowSet']
shot_df = pd.DataFrame(shots, columns=headers)

def draw_court(ax=None, color='black', lw=2):
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

    # The paint
    # Create the outer box 0f the paint, width=16ft, height=19ft
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)
    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color, fill=False)

    # free throw box
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180, linewidth=lw, color=color, fill=False)
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color, linestyle='dashed')
    
    # Restricted Zone
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw, color=color)

    # Three point line
    corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw, color=color)
    corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color)

    # Center Court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0, linewidth=lw, color=color)

    # List of the court elements to be plotted
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc, center_outer_arc,
                      center_inner_arc]

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    return ax

sns.set_style("white")
sns.set_color_codes()
plt.figure(figsize=(6,5.5))
plt.scatter(shot_df.LOC_X, shot_df.LOC_Y)
draw_court()
plt.xlim(-250,250)
plt.ylim(422.5, -47.5)
plt.show()