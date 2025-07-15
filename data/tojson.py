import pandas as pd
csv_file = '2024-Health4Me GP Network.csv'
json_file = 'gps.json'

df = pd.read_csv(csv_file, header=None)
df.columns = df.iloc[0]
df = df[1:]
df.to_json('gps.json', orient='records')