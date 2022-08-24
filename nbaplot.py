import nba_api
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nba_api.stats.endpoints import teamgamelogs
from nba_api.stats.static import teams

#seasons taken from 2011 to 2022
seasons = []
for i in range(11,22):
    seasons.append(f'20{i}-{i+1}')
wins =[]
#loop that takes on seasons and a nba team and extracts certain stats into lists
for season in seasons:
    a = teamgamelogs.TeamGameLogs(season_nullable= season, team_id_nullable= '1610612744')
    a_df = a.get_data_frames()[0]
    aa = pd.DataFrame(a_df)
    stats = aa[['WL','PTS','AST','REB','TOV','FG3M','FG3A','FTM','OREB','FG_PCT']]
    print(stats)
    wins_lose = aa['WL']
    wins_lose_counts = wins_lose.value_counts()
    win_count = wins_lose_counts['W']
    wins.append(win_count)
    pts_col = stats['PTS']
    pts = pts_col.tolist()
    ast_col = stats['AST']
    ast = ast_col.tolist()
    ftm_col = stats['FTM']
    ftm = ftm_col.tolist()
    oreb_col = stats['OREB']
    oreb = oreb_col.tolist()
    #plots a linear regression model for any two variables for the span of the seasons
    sns.lmplot(x= 'TOV', y= 'FG_PCT', hue = 'WL', data=stats)
    plt.show()
    
    





