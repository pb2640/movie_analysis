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
import sys
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer

class ProcessDataframe():
    def __init__(self, df_path) -> None:
    
        try:
            self.df = pd.read_csv(df_path)
        except Exception as e:
            print("There was a problem in reading the file. The following error occured: {}".format(e))
            sys.exit(1)

    def remove_columns(self, columns_to_include: list):
        columns_to_include_final = []
        for col in columns_to_include:
            if col in self.df.columns:
                columns_to_include_final.append(col)

        self.df = self.df[columns_to_include_final]

    def remove_na_rows(self, na_col_list):
        for col in na_col_list:
            self.df = self.df[self.df[col].notna()]
    def convert_str_to_list(self,input_str):
        try:
            return eval(input_str)
        except:
            return []
    
    def reduce_categorical_variables_dimensions(self, variable_name, threshold):
        if(variable_name not in self.df.columns):
            print("No such variable name")
            return
        if(isinstance(self.df[variable_name][self.df.index[0]],str)):
            self.df[variable_name] = self.df[variable_name].apply(self.convert_str_to_list)
        flattened_column = self.df[variable_name].explode()
        try:    
            column_value_counts = flattened_column.value_counts()
        except Exception as e:
            print("Make sure your column values are in a list format")
            #take only those values which are greater than a threshold
            return
        try:
            values_list = column_value_counts[column_value_counts>threshold].index
        except:
            print("Error with  the value counts obj")
            return 
        values_set = set(values_list)
        # iterate over the df and 
        # replace any value in the list if it is not in the values set
        for i in self.df.index:
            if(not self.df[variable_name][i]):
                self.df[variable_name][i] = []
                continue
            curr_row = self.df[variable_name][i]
            for j in range(len(curr_row)):
                if(curr_row[j] not in values_set):
                    curr_row[j] = "Others"
            
            self.df[variable_name][i] = list(set(self.df[variable_name][i]))
    
    def encode_variable(self, col_name):
        mlb = MultiLabelBinarizer(sparse_output=True)
        curr_df = self.df.copy()
        new_df = curr_df.join(
                pd.DataFrame.sparse.from_spmatrix(
                    mlb.fit_transform(curr_df.pop(col_name)),
                    index=curr_df.index,
                    columns=mlb.classes_))
        return new_df





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
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=test_size, random_state=42)
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
        self.test_mse = mean_squared_error(self.y_test, self.y_pred)
        self.test_r2 = r2_score(self.y_test, self.y_pred)
        

    def report_model_results(self):
        print("Time taken to train the model {} seconds".format(self.total_time_taken_to_train_model))
        self.model_results = {"test_mse": self.test_mse, "test_r2_score": self.test_r2 }
        print(self.model_results)


    def inference(self, input_dict : dict):
        '''
        Provide the input to the model and get the prediction
        '''
        self.inference_input_dict = input_dict
        inference_input_list = [0]*len(self.X.columns)
        for it in input_dict:
            if it in self.X.columns:
                index = self.X.columns.get_loc(it)
                inference_input_list[index] = input_dict[it]
        try:
            inference_input_list = np.array(inference_input_list)
            self.inference_prediction = self.model.predict(inference_input_list.reshape(1, -1))
        except Exception as e:
            print("The following error occured while inferencing the model : {}".format(e))
            return None     
        return self.inference_prediction







