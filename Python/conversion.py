import json
import pandas as pd
jsondata = pd.read_json("./j.json")
jsondata.to_csv("./sheets.csv",index=None)