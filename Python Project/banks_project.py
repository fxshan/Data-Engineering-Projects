import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

url = 'https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Name', 'MC_USD_Billion']
output_path = './Largest_banks_data.csv'
csv_path = './exchange_rate.csv'
db_name = 'Banks.db'
table_name = 'Largest_banks'

def log_progress(message):
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open('./code_log.txt', 'a') as f:
        f.write('<' + timestamp + '> : <' + message + '>\n')

def extract(url, table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns = table_attribs)
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    rows = rows[1:]

    for row in rows:
        cols = row.find_all('td')
        if len(cols) != 0:
            a_tags = cols[1].find_all('a')
            tag = a_tags[1]
            data_dict = {'Name':tag.contents[0],
                        'MC_USD_Billion':cols[2].contents[0][:-1]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
    return df

def transform(df, csv_path):
    # get exchange rates
    rates = pd.read_csv(csv_path)
    rates_dict = rates.set_index('Currency').to_dict()['Rate']
    # transform string to float
    data_list = df['MC_USD_Billion'].tolist()
    float_list = []
    for x in data_list:
        data_str = ''.join(x.split('.'))
        float_list.append(np.round(float(data_str)/100, 2))

    df['MC_USD_Billion'] = float_list
    df['MC_GBP_Billion'] = [np.round(x*rates_dict['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*rates_dict['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*rates_dict['INR'],2) for x in df['MC_USD_Billion']]
    return df

def load_to_csv(df, output_path):
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output= pd.read_sql(query_statement, sql_connection)
    print(query_output)

# testing
log_progress('Preliminaries complete. Initiating ETL process')
df = extract(url, table_attribs)
log_progress('Data extraction complete. Initiating Transformation process')
df = transform(df, csv_path)
log_progress('Data transformation complete. Initiating Loading process')
load_to_csv(df, output_path)
log_progress('Data saved to CSV file')
conn = sqlite3.connect(db_name)
log_progress('SQL Connection initiated')
load_to_db(df, conn, table_name)
log_progress('Data loaded to Database as a table, Executing queries')
query1 = 'SELECT * FROM Largest_banks'
query2 = 'SELECT AVG(MC_GBP_Billion) FROM Largest_banks'
query3 = 'SELECT Name from Largest_banks LIMIT 5'
run_query(query1, conn)
run_query(query2, conn)
run_query(query3, conn)
log_progress('Process Complete')
conn.close()
log_progress('Server Connection closed')
