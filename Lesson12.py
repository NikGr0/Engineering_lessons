import requests
import pandas as pd


api_key = '1bbd0e4feae573037172783bf5a5ac2b'
source = 'RUB'
start_date = '2024-03-01'
end_date = '2023-03-20'
URL = f'http://api.currencylayer.com/historical?access_key={api_key}&date={start_date}&source={source}'
#r = requests.get(url=URL)
# result = r.json()
# print(result)
# print(result.get('quotes'))
# print(result.get('quotes').get('USDGBP'))
# print(result.get('quotes').get('USDEUR'))

res1 = []

for i in ['2024-03-01', '2024-04-01']:
    URL = f'http://api.currencylayer.com/historical?access_key={api_key}&date={i}&source={source}'
    r = requests.get(url=URL)
    result = r.json()
    res1.append(result.get('quotes'))

print(res1)



df1 = pd.DataFrame(res1)
df1.to_csv('kurs_csv.csv')