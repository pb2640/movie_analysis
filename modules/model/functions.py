'''
This file is reproducible
- Flow
    - Provide a dataset as input with the target variable
    - The dataset is divided into train and test
    - Define if its a regression problem or a classification problem
    - Train the model
    - Show the time taken to train the model
    - Return Validation results and other results if applicable TODO
    - Provide a way to inference the model
'''

# import modules
import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Provide the dataset and the target variable
class Model():
    def __init__(self, df, target_variable, problem_type) -> None:
        if (not isinstance(df, pd.DataFrame)):
            raise ValueError
        if (not isinstance(target_variable, str)):
            raise ValueError
        if (not isinstance(problem_type, str)):
            raise ValueError
        if (target_variable not in df.columns):
            print("{} not in columns of df".format(target_variable))
        self.df = df
        self.target_variable = target_variable
        self.problem_type = problem_type
        self.model_results = {}
    
    def prepare_train_test_datasets(self, test_size=0.2):
        '''
        Provide test size, default is 0.2
        '''
        self.X = self.df.drop(self.target_variable, axis=1)  # Features (all columns except "budget")
        self.y = self.df[self.target_variable]  # Target variable

        try:
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size, random_state=42)
        except Exception as e:
            print("The following error occured while preparing the dataset {}".format(e))
    
    def train_model(self):
        # Create a Linear Regression model

        self.model = LinearRegression()
        self.model_train_start_time = time.time()
        # Fit the model to the training data
        self.model.fit(self.X_train, self.y_train)
        self.model_train_end_time = time.time()
        # Make predictions on the test set
        
        self.total_time_taken_to_train_model = self.model_train_end_time - self.model_train_start_time

    def test_model(self):
        self.y_pred = self.model.predict(self.X_test)
        self.mse = mean_squared_error(self.y_test, self.y_pred)
        self.r2 = r2_score(self.y_test, self.y_pred)
        

    def report_model_results(self):
        self.model_results = {"mse": self.mse,"r2_score":self.r2}
        print(pd.DataFrame)


    def inference(self, input_list):
        '''
        Provide the input to the model and get the prediction
        '''
        self.inference_input = input_list
        try:
            self.inference_prediction = self.model.predict(input_list)
        except Exception as e:
            print("The following error occured while inferencing the model {}".format(e))
            return None
        
        
        return self.inference_prediction







