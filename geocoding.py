import requests 
import urllib.parse
import json
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()
API = os.getenv("API_KEY")

df = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/main/WK7/assignment7_slim_hospital_addresses.csv")
df['GEO'] = df['ADDRESS'] + ' ' + df['CITY'] + ' ' + df['STATE']
df_s = df.sample(n=100) #sample



