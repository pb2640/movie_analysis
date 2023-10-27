<<<<<<< HEAD
import sys

def make_new_columns_boxOffice(curr_df,col_name, list_of_keys):
=======
"""
This script contains all functions

The following guidelines must be implemented for best practices:

-> Include Comment after declaring a function, this will act as
docstring when this functions is called
-> Run Flake8 after every commit
-> Run black after every commit

TODO : Log errors

"""
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer


def make_new_columns_boxOffice(orig_df, col_name, list_of_keys):
>>>>>>> 4f6298f9e3b7888b55495006822cb7b1a7a39c1a
    """
    params will be(col_name,[list_of_keys]) ,
    the names in the list should be same as keys
    """
<<<<<<< HEAD
    if(col_name not in curr_df.columns):
=======
    curr_df = orig_df.copy()
    if (col_name not in curr_df.columns):
>>>>>>> 4f6298f9e3b7888b55495006822cb7b1a7a39c1a
        print("No such column exists in the df")
    for key in list_of_keys:
        curr_df[key] = ""
    for i in range(len(curr_df)):
        response_list = eval(curr_df["boxOffice"][i])
<<<<<<< HEAD
        if(response_list):
=======
        if (response_list):
>>>>>>> 4f6298f9e3b7888b55495006822cb7b1a7a39c1a
            response = response_list
            for it in response:
                for key in list_of_keys:
                    if key in it:
<<<<<<< HEAD
                        curr_df[key][i] = it[key]["val"]
                        

    return curr_df
    
    # delete the original column 

def make_new_columns_first(curr_df, col_name, list_of_keys):
=======
                        curr_df[key][i] = it[key]["val"]       
    return curr_df


def make_new_columns_first(orig_df, col_name, list_of_keys):
>>>>>>> 4f6298f9e3b7888b55495006822cb7b1a7a39c1a
    """
    params will be(col_name,[list_of_keys]) ,
    the names in the list should be same as keys
    """
<<<<<<< HEAD
=======
    curr_df = orig_df.copy()
>>>>>>> 4f6298f9e3b7888b55495006822cb7b1a7a39c1a
    if (col_name not in curr_df.columns):
        print("No such column exists in the df")
    for key in list_of_keys:
        curr_df[key] = ""
    for i in range(len(curr_df)):
        response_list = eval(curr_df["first"][i])
        if (response_list):
            response = response_list
            for it in response:
                for key in list_of_keys:
                    if key in it:
<<<<<<< HEAD
                        curr_df[key][i] = it[key]
    return curr_df
   

def money_str_to_currency(input_str):
    '''Takes an input as a str. Saves currency signs if any\n",
    saves value'''
    if(len(input_str)==0):
        return None
    #strip the str of any spaces\n",
    stripped_input_str = input_str.strip()
    split_str = stripped_input_str.split()
    money_str = split_str[0]
    currency = money_str[:1]
    # money_with_comma = money_str[1:]
    # money = money_with_comma.replace(",","")
    return currency

def money_str_to_int(input_str):
    '''Takes an input as a str. Saves currency signs if any\n",
    saves value'''
    if(len(input_str)==0):
        return None
    #strip the str of any spaces\n",
    stripped_input_str = input_str.strip()
    split_str = stripped_input_str.split()
    money_str = split_str[0]
    currency = money_str[:1]
    money_with_comma = money_str[1:]
    money = money_with_comma.replace(",","")
    return money

def extract_techspecs(input_str):
    try:
        if (len(input_str) == 0):
            return [None, None, None]
        input_list = eval(input_str)
        '''iterate on every object,
        find every key in every object,
        if you find it place the value 
        else place None'''
        runtime = None
        soundmix = None
        aspect_ratio = None
        for obj in input_list:
            if ("title-techspec_runtime" in obj):
                runtime = obj["title-techspec_runtime"]["val"]
            if ("title-techspec_soundmix" in obj):
                soundmix = obj["title-techspec_soundmix"]["val"]
            if ("title-techspec_aspectratio" in obj):
                aspect_ratio = obj["title-techspec_aspectratio"]["val"]
    except Exception as e:
        print(input_str, e)
        sys.exit(1)
    return [runtime, soundmix, aspect_ratio]
        
            
=======
                        curr_df[key][i] = it[key]                
    return curr_df


def make_new_columns_details(orig_df, col_name, list_of_keys):
    """
    params will be(col_name,[list_of_keys]) ,
    the names in the list should be same as keys
    """
    curr_df = orig_df.copy()
    if (col_name not in curr_df.columns):
        print("No such column exists in the df")
    for key in list_of_keys:
        curr_df[key] = ""
    for i in range(len(curr_df)):
        response_list = eval(curr_df["details"][i])
        if (response_list):
            response = response_list
            for it in response:
                for key in list_of_keys:
                    if key in it:
                        curr_df[key][i] = it[key]["val"]
    return curr_df


def encode_variable(orig_df, col_name):
    mlb = MultiLabelBinarizer(sparse_output=True)
    curr_df = orig_df.copy()
    curr_df = curr_df.join(
            pd.DataFrame.sparse.from_spmatrix(
                mlb.fit_transform(curr_df.pop(col_name)),
                index=curr_df.index,
                columns=mlb.classes_))
    return curr_df
>>>>>>> 4f6298f9e3b7888b55495006822cb7b1a7a39c1a