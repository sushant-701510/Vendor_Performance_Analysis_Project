
import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingesting_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def ingest_db(df,table_name,engine):
     '''THIS FUNCTION WILL INGEST THE DATAFRAME INTO DATABASE TABLE'''
     df.to_sql(table_name,con=engine, if_exists='replace',index= False)

def load_raw_data():
    ''' THIS FUNCTION WILL LOAD THE CSV AS DATAFRAME AND INGEST INTO DB'''
    
    start=time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df=pd.read_csv('data/'+file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df,file[:-4],engine)
    end = time.time()
    total_time = (end-start)/60
    logging.info('-------------------Ingestion Complete----------------------')

    logging.info(f'\nTotal Time Taken: {total_time} minutes')


if __name__== '__main__' :   
    load_raw_data()
        
    

