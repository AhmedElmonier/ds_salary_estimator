
import glassdoor_scraper as gs 
import pandas as pd 

path = '/media/monier/Data/my_projects/Data Science/chromedriver'

df = gs.get_jobs('data scientist', 10000, False, 7, path)

df.to_csv('glassdoor_ds_new.csv', index=False)