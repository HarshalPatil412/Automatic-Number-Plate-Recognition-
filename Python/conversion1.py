import json
import pandas as pd
       
dictionary ={  
  "id": "42",  
  "name": "harshal",  
  "department": "IT"
}  
       
json_object = json.dumps(dictionary, indent = 4)  
print(json_object) 

