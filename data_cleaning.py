import pandas as pd


pd.set_option('display.max_columns', None)  
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

df = pd.read_csv('glassdoor_ds.csv')


# Cleaning
df = df[df['Salary Estimate'] != '-1']
df['Hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['Company Provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = min_hr.apply((lambda x: int(x.split('-')[0])))
df['max_salary'] = min_hr.apply((lambda x: int(x.split('-')[1])))
df['avg_salary'] = (df['min_salary']+df['max_salary'])/2

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis=1)
df['state'] = df['Location'].apply(lambda x: x.split(', ')[-1:])
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)
df['company_age'] = df.Founded.apply(lambda x: x if x <0 else 2020 - x)
df['python'] = df['Job Description'].apply((lambda x: 1 if 'python' in x.lower() else 0))
df['r_studio'] = df['Job Description'].apply((lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0))
df['spark'] = df['Job Description'].apply((lambda x: 1 if 'spark' in x.lower() else 0))
df['aws'] = df['Job Description'].apply((lambda x: 1 if 'aws' in x.lower() else 0))
df['excel'] = df['Job Description'].apply((lambda x: 1 if 'excel' in x.lower() else 0))

def title_simplifier(title):
    if 'data scientist' in title.lower():
        return 'data scientist'
    elif 'data engineer' in title.lower():
        return 'data engineer'
    elif 'analyst' in title.lower():
        return 'analyst'
    elif 'machine learning' in title.lower():
        return 'mle'
    elif 'manager' in title.lower():
        return 'manager'
    elif 'director' in title.lower():
        return 'director'
    else:
        return 'na'
    
def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower():
        return 'jr'
    else:
        return 'na'

df['job_simp'] = df['Job Title'].apply(title_simplifier)
df['seniority'] = df['Job Title'].apply(seniority)
df['desc_len'] = df['Job Description'].apply(lambda x: len(x))
df['num_comp'] = df['Competitors'].apply(lambda x: len(x.split(',')) if x != '-1' else 0)

#hourly wage to annual 

df['min_salary'] = df.apply(lambda x: x.min_salary*2 if x.Hourly ==1 else x.min_salary, axis =1)
df['max_salary'] = df.apply(lambda x: x.max_salary*2 if x.Hourly ==1 else x.max_salary, axis =1)
df['company_txt'] = df.company_txt.apply(lambda x: x.replace('\n', ''))

df.to_csv('salary_data.csv', index=False)
df2 = pd.read_csv('salary_data.csv')

print(df2.head())