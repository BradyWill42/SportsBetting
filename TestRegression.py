from nba_api.stats.endpoints import scoreboard
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer



# Load your historical game data
game_logs = pd.read_csv('nbaHomeWinLossModelDataset.csv', header=0)

def get_games_for_today():
    today_games = scoreboard.Scoreboard().get_dict()
    if 'resultSets' in today_games:
        games_today = pd.DataFrame(today_games['resultSets'][0]['rowSet'], columns=today_games['resultSets'][0]['headers'])
        return games_today
    else:
        return pd.DataFrame()

today_games = get_games_for_today()

today_games.to_excel('today_games.xlsx', index=False)

previousGameArray = []

for i in range(len(today_games['HOME_TEAM_ID'])):
    print(today_games['HOME_TEAM_ID'][i])
    largestDate = game_logs['GAME_DATE'][1]
    rowOfDate = 1
    for j in range(len(game_logs["HOME_TEAM_ID"])):
        if today_games['HOME_TEAM_ID'][i] == game_logs['HOME_TEAM_ID'][j]:
            if game_logs['GAME_DATE'][j] > largestDate:
                largestDate = game_logs['GAME_DATE'][j]
                rowOfDate = j
    print(largestDate)
    previousGameArray.append(game_logs['HOME_LAST_GAME_OE'][rowOfDate])
    previousGameArray.append(game_logs['HOME_LAST_GAME_HOME_WIN_PCTG'][rowOfDate])
    previousGameArray.append(game_logs['HOME_NUM_REST_DAYS'][rowOfDate])
    previousGameArray.append(game_logs['HOME_LAST_GAME_AWAY_WIN_PCTG'][rowOfDate])
    previousGameArray.append(game_logs['HOME_LAST_GAME_TOTAL_WIN_PCTG'][rowOfDate])
    previousGameArray.append(game_logs['HOME_LAST_GAME_ROLLING_SCORING_MARGIN'][rowOfDate])
    previousGameArray.append(game_logs['HOME_LAST_GAME_ROLLING_OE'][rowOfDate])
    previousGameArray.append(game_logs['HOME_W'][rowOfDate])


previousGameArray.insert(0,['HOME_LAST_GAME_OE', 'HOME_LAST_GAME_HOME_WIN_PCTG', 'HOME_NUM_REST_DAYS'])
previousGameArray.insert('HOME_LAST_GAME_TOTAL_WIN_PCTG'[0])
previousGameArray.insert('HOME_LAST_GAME_ROLLING_SCORING_MARGIN'[0])
previousGameArray.insert('HOME_LAST_GAME_ROLLING_OE'[0])
previousGameArray.insert('HOME_W'[0])
print(previousGameArray[0])

    




