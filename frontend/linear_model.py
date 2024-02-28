import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin 
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline 
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV 
from sklearn.model_selection import train_test_split 

class DictEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X: pd.DataFrame, y=None):
        return self
    
    def parseList(self, holdlist: list[str]):
        """ Parses a list of holds into a dicionary of the form {hold : 1} """
        return {hold : 1 for hold, color in holdlist}
    
    def transform(self, X: pd.DataFrame):
        """
        Encodes a list of holds into a dictionary of key, value pairs where
        each key is a hold of the form [column index A-K][row index 1-18]
        and each value is 1
        """
        X = X.dropna() # first drop missing values (problem no longer exists)
        #X['holds'] = X['holds'].apply(lambda holdlist: self.parseList(eval(holdlist))) # parse strings to list of holds
        X['holds'] = X['holds'].apply(lambda holdlist: self.parseList(holdlist)) # parse strings to list of holds
        return X['holds']
    
class LabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.grade_dict = {
                '5+' : 0,
                '6A' : 1,
                '6A+' : 2,
                '6B' : 3,
                '6B+' : 4,
                '6C' : 5,
                '6C+' : 6,
                '7A' : 7,
                '7A+' : 8,
                '7B' : 9,
                '7B+' : 10,
                '7C' : 11,
                '7C+' : 12,
                '8A' : 13,
                '8A+' : 14,
                '8B' : 15,
                '8B+' : 16,
                '8C' : 17,
                '8C+' : 18
            }
    def fit(self, X: pd.DataFrame, y=None):
        return self
    
    def grade_to_number(self, grade: str) -> int:
        """ Maps a route's grade to an integer """

        if grade not in self.grade_dict:
            raise Exception(f"Invalid Grade! {grade}")
        else:
            return self.grade_dict[grade]
    
    def transform(self, X: pd.DataFrame):
        """ Maps the `grades` column of a `DataFrame` to its numeric value (to be scaled) """
        X = X.dropna()
        X['grades_numeric'] = X['grades'].apply(self.grade_to_number) # parse grades to numeric value
        return X[['grades_numeric']]