# import requests
#
# download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
# target_csv_path = "nba_all_elo.csv"
#
# response = requests.get(download_url)
# response.raise_for_status()    # Check that the request was successful
# with open(target_csv_path, "wb") as f:
#     f.write(response.content)
# print("Download ready.")

import pandas as pd


# nba_data = pd.read_csv('nba_all_elo.csv')
# print(type(nba_data))
# print(len(nba_data))
# print(nba_data.shape)

# print(nba_data.head())
# print(nba_data.tail())

# print(nba_data.info())
# print(nba_data['pts'].describe())
# print()

# print(nba_data['team_id'].value_counts())
# print(nba_data['fran_id'].value_counts())

# print(nba_data.loc[nba_data['fran_id'] == 'Lakers', 'team_id'].value_counts())
#
# print()

# nba_data['date_played'] = pd.to_datetime((nba_data['date_game']))
# print(nba_data.loc[nba_data['team_id'] == 'MNL', 'date_played'].min())

# print(nba_data.loc[nba_data['team_id'] == 'MNL', 'date_played'].max())

# print(nba_data.loc[nba_data['team_id'] == 'MNL', 'date_played'].agg(('min', 'max')))

# PANDAS -> PANDAS IN PYTHON - ANALYZE

# #########################################################
# url request -> response
# api - REST-API - application programming interface (API)
import requests

# url = 'https://api.github.com/'
# response = requests.get(url)
# print(response)
# print(response.status_code)

# Method
# GET ->  api.examples/customers , api.examples/customers/<customer_id>
# POST ->
# PUT ->
# PATCH
# DELETE

# 2xx  OK
# 3xx  Redirection
# 4xx  Client Error - 400, 401 , 404 Not found ,
# 5xx  Server Error - 503

# url = 'https://api.github.com/'
# url = 'https://api.github.com/search/commits?q=felan'
# response = requests.get(url)
#
# print(response.headers)
# print(response.json())
# a = response.json()
# for item in a['items']:
#     print(item)


# response = requests.get('https://api.github.com/search/repositories',
#                         params=[('q', 'requests+language:python')])
# # print(response.json())
# a = response.json()
# for item in a['items']:
#     print(item)


# response = requests.get('https://api.github.com/repos/hoomanjb/python-kids-class-codes')
# # print(response.json())
# a = response.json()
# # print(a)
# for item in a.items():
#     print(item)