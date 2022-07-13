import pandas as pd
df_json = pd.read_json("j.json")
df_json.to_excel("j.xlsx")