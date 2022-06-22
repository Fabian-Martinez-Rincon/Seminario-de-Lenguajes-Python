import pandas as pd     
import os 

EVENTS_PATH =  os.path.join(os.path.abspath('..'),'src','database','events','events.csv') 

data_frame = pd.read_csv(EVENTS_PATH,encoding='utf-8',index_col='timestamp')
print(data_frame)