#Modular Coding

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass  #a decorator, used to define a class variable w/o using __init__
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifacts","train.csv") #all the files will be saved in this path
    test_data_path: str=os.path.join("artifacts","test.csv") #all the files will be saved in this path
    raw_data_path: str=os.path.join("artifacts","raw.csv")   #al the ll be saved in this path
  #these are the inputs i am giving to my data ingestion component and ingestion component knows where to save train,test,raw data path becoz of the mentioned path
  #artifacts is a folder that i will create using os.makedirs() later


#starting the class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    #home fn:
    def initiate_data_ingestion(self): #this will consist code to read data from other databases
        #usually from utlis file where mongodb, sql client are there
        logging.info("Enter the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv') #can also use mongodb, sql
            logging.info('Read the dataset as dataframe') #make sure to keep on writing logs, becoz wherever the exception takes place, I can get to know through logs
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False,header=True) #saving to csv

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False,header=True) #train test split is done, now I am saving in artifact folder
            train_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True)

            logging.info("Data ingestion has happened!")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,

                

            )
        except Exception as e:
            raise CustomException(e,sys) #raise CustomException with e,sys
        
        

#initiating and running:--

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion() #now u can see artifacts folder being created
    # Execute by typing python src/components/data_ingestion.py in cmd terminal
    #write .artifacts under environments in gitignore file






