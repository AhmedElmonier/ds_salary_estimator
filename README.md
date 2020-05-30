# Data Science Salary Estimator: Project Overview
* Created a tool that estimates data science salaries to help me and other data scientists collegues who is interested in it to negotiate their income when they get a job.
* Scraped over 1500 job descriptions from glassdoor using python and selenium.
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask

## Idea & Credit

the original idea was to help me how much a data scientist estimate salary is and help me negoitiate. i searched on how to scrape Linkedin but i found it might be very hard, then i found this guy on youtube how made the same excat as tutorial and followed him in this journy.

YouTube Project Walk-Through by Ken lee: https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

original Walk-Through Glassdoor Scraper artilcle: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

## Web Scraping

i used the web scraper github repo (above) to scrape 1500 job postings from glassdoor.com. With each job, we got the following:

* Job title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Headquarters
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

## Data Cleaning

After scraping the data, I followed *ken* to clean it up so that it was usable for the model. we made the following changes and created the following variables:

* Parsed numeric data out of salary
* Made columns for employer provided salary and hourly wages
* Removed rows without salary
* Parsed rating out of company text
* Made a new column for company state
* Added a column for if the job was at the company’s headquarters
* Transformed founded date into age of company
* Made columns for if different skills were listed in the job description:
  * Python
  * R
  * Excel
  * AWS
  * Spark
* Column for simplified job title and Seniority
* Column for description length
