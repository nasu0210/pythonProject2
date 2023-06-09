import pandas as pd
df = pd.read_excel('c:/data3/days000.xlsx')
expanded_rows = []

for _, row in df.iterrows():
    value = row['Value']
    expanded_rows.extend([row] * value)

expanded_df = pd.DataFrame(expanded_rows)
print(expanded_df.to_string())
print(expanded_df['Value'].count())
expanded_df.to_excel('c:/data3/days0000.xlsx', index=False)