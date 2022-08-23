from sys import api_version
import nba_api
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier, kneighbors_graph
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

from nba_api.stats.endpoints import teamgamelogs

#creating a list of seasons from 2011 to 2022
seasons = []
for i in range(11,22):
    seasons.append(f'20{i}-{i+1}')

#making a loop where it takes in the year and a specific team in which a data frame is displayed
full = []
for season in seasons:
    team_log= teamgamelogs.TeamGameLogs(season_nullable= season, team_id_nullable= '1610612744')
    team_log_df = team_log.get_data_frames()[0]
    team_stats = pd.DataFrame(team_log_df)
    team_stats['WL_int'] = (team_stats['WL'] == 'W').astype('int')
    four_factors = team_stats[['TOV','FTM','OREB','FG_PCT','WL_int']]
    full.append(four_factors)
#concatenating all dataframes into one big dataframe
full_season = pd.concat(full)
    
#splitting the dataset into test, train  
X = full_season.iloc[:,0:4]
y = full_season.iloc[:,4]
X_train, X_test, y_train,y_test = train_test_split(X,y, random_state = 0,test_size= 0.2)

#scaling the test, train data
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


#found n_neighbors by sqrt(len(y))
classifier = KNeighborsClassifier(n_neighbors=7,p=2,metric = 'euclidean')

classifier.fit(X_train,y_train)

#predicting test results
y_pred = classifier.predict(X_test)
print(y_pred)

#Evaluate Model
cm = confusion_matrix(y_test,y_pred)
print(cm)

print('The F1 score is', f1_score(y_test,y_pred))
print('The accuracy score is',accuracy_score(y_test,y_pred))




    

   
