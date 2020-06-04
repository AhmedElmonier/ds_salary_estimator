
import glassdoor_scraper as gs 
import pandas as pd 

path = 'D:/my_projects/DS_project/chromedriver'

df = gs.get_jobs('data scientist', 10000, False, 4, path)
df.to_csv('glassdoor_ds_10000.csv', index=False)
