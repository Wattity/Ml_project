import sys
import os
from dataclasses import dataclass

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.execption import CustomException
from src.logger import logging

@dataclass
class DataTransformationconfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transfomation_config=DataTransformationconfig()
    def get_data_trasformer_obj(self):
        '''
        This function is responsible for data transformation
        '''

        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipeline=Pipeline(
                steps=[
                    ("inputer",SimpleImputer(strategy="medain")),
                    ("scaler",StandardScaler())


                ]
            )
            cal_pipeline=Pipeline(

                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequency")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler())

                ]
            )
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")
            
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns)
                    ("cal_pineline",cal_pipeline,categorical_columns)
                ]
            )

    def initiate_data_transformation():
            try:
                 train_df=pd.read_csv("")
                 test_df=pd.read_csv("")
                 preprossing_obj=
            except:
                 pass
            
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)