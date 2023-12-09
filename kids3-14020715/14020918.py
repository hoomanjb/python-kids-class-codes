# REGEX
# Pandas , numpy

# import pandas
# import requests

# download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
# target_csv_path = "nba_all_elo.csv"
#
# response = requests.get(download_url)
# response.raise_for_status()    # Check that the request was successful
# with open(target_csv_path, "wb") as f:
#     f.write(response.content)
# print("Download ready.")

# import pandas as pd
#
# nba = pd.read_csv('nba_all_elo.csv')
# nba = pd.read_excel('nba_all_elo.xlsx')
#
# pd.set_option('display.max.columns', None)
# print(type(nba))
# print(len(nba))
# print(nba.shape)
# print(nba.head())
# print(nba.tail())
# print(nba.info())
# print(nba.describe())

# print(nba['team_id'].value_counts())
# print('-------------------------')
# print(nba['fran_id'].value_counts())

# print(nba.loc[nba['fran_id'] == 'Lakers', 'team_id'].value_counts())
# #################################

# Regex  regular expressions
import re

text = 'foo45681239bar'
print('123' in text)

# print(re.search('123', text))
# print(re.search('[0-9][0-9][0-9]', text))
#
# print(re.search('[0-9][0-9][0-9]$', 'asdasd123'))
# print(re.search('^[0-9][0-9][0-9]$', '123'))
# print(re.search('^\d{10}$', '1234567890'))

# print(re.search('1.3', 'foo1gsas3bar'))
# print(re.search('1*3', 'foo1453bar'))
# print(re.search('1+3', 'foo13bar'))
# print(re.search('1?3', 'foo13bar'))
# ∙ Matches zero or one repetition
# ∙ Specifies the non-greedy versions of *, +, and ?
# ∙ Introduces a lookahead or lookbehind assertion
# ∙ Creates a named group

print(re.search('ba[artz]', ))
print(re.search('ba[^artz]', ))
print(re.search('ba[a-z]', ))
print(re.search('ba[ar][0-9]', ))
print(re.search('^$', ))