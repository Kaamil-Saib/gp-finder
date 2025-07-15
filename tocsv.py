import pandas as pd

excel_file = '2024-Health4Me GP Network.xlsx'
csv_file = '2024-Health4Me GP Network.csv'

df = pd.read_excel(excel_file)

df.to_csv(csv_file, index=False)