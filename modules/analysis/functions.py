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
        response_list = eval(curr_df["boxOffice"][i])
        if (response_list):
            response = response_list
            for it in response:
                for key in list_of_keys:
                    if key in it:
                        curr_df[key][i] = it[key]["val"]       
    return curr_df


def make_new_columns_first(orig_df, col_name, list_of_keys):
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
        response_list = eval(curr_df["first"][i])
        if (response_list):
            response = response_list
            for it in response:
                for key in list_of_keys:
                    if key in it:
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
