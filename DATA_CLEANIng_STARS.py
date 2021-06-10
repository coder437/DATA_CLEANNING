import pandas as pd
df=pd.read_csv('stars_data.csv')
print(df.shape)
df.delete("Lumiosity")
df.to_csv('main.csv')