"""
This script contains all functions

The following guidelines must be implemented for best practices:

-> Include Comment after declaring a function, this will act as
docstring when this functions is called
-> Run Flake8 after every commit
-> Run black after every commit

TODO : Log errors

"""
import sys
import re
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer


def make_new_columns_boxOffice(curr_df, col_name, list_of_keys):
    """ """
    if col_name not in curr_df.columns:
        print("No such column exists in the df")
    for key in list_of_keys:
        curr_df[key] = ""
    for i in range(len(curr_df)):
        response_list = eval(curr_df["boxOffice"][i])
        if response_list:
            response = response_list
            for it in response:
                for key in list_of_keys:
                    if key in it:
                        curr_df[key][i] = it[key]["val"]

    return curr_df

    # delete the original column


def make_new_columns_first(curr_df, col_name, list_of_keys):
    """
    params will be(col_name,[list_of_keys]) ,
    the names in the list should be same as keys
    """
    if col_name not in curr_df.columns:
        print("No such column exists in the df")
    for key in list_of_keys:
        curr_df[key] = ""
    for i in range(len(curr_df)):
        response_list = eval(curr_df["first"][i])
        if response_list:
            response = response_list
            for it in response:
                for key in list_of_keys:
                    if key in it:
                        curr_df[key][i] = it[key]
    return curr_df


def make_new_columns_details(curr_df, col_name, list_of_keys):
    """
    params will be(col_name,[list_of_keys]) ,
    the names in the list should be same as keys
    """
    if col_name not in curr_df.columns:
        print("No such column exists in the df")
    for key in list_of_keys:
        curr_df[key] = ""
    for i in range(len(curr_df)):
        response_list = eval(curr_df["details"][i])
        if response_list:
            response = response_list
            for it in response:
                for key in list_of_keys:
                    if key in it:
                        curr_df[key][i] = it[key]["val"]

    return curr_df


def money_str_to_currency(input_str):
    """Takes an input as a str. Saves currency signs if any\n",
    saves value"""
    if len(input_str) == 0:
        return None
    # strip the str of any spaces\n",
    stripped_input_str = input_str.strip()
    split_str = stripped_input_str.split()
    money_str = split_str[0]
    currency = money_str[:1]
    # money_with_comma = money_str[1:]
    # money = money_with_comma.replace(",","")
    return currency


def money_str_to_int(input_str):
    """Takes an input as a str. Saves currency signs if any\n",
    saves value"""
    if len(input_str) == 0:
        return None
    # strip the str of any spaces\n",
    stripped_input_str = input_str.strip()
    split_str = stripped_input_str.split()
    money_str = split_str[0]
    currency = money_str[:1]
    money_with_comma = money_str[1:]
    money = money_with_comma.replace(",", "")
    return money


def extract_techspecs(input_str):
    try:
        if len(input_str) == 0:
            return [None, None, None]
        input_list = eval(input_str)
        """iterate on every object,
        find every key in every object,
        if you find it place the value 
        else place None"""
        runtime = None
        soundmix = None
        aspect_ratio = None
        for obj in input_list:
            if "title-techspec_runtime" in obj:
                runtime = obj["title-techspec_runtime"]["val"]
            if "title-techspec_soundmix" in obj:
                soundmix = obj["title-techspec_soundmix"]["val"]
            if "title-techspec_aspectratio" in obj:
                aspect_ratio = obj["title-techspec_aspectratio"]["val"]
    except Exception as e:
        print(input_str, e)
        sys.exit(1)
    return [runtime, soundmix, aspect_ratio]


def make_new_columns_details(orig_df, col_name, list_of_keys):
    """
    params will be(col_name,[list_of_keys]) ,
    the names in the list should be same as keys
    """
    curr_df = orig_df.copy()
    if col_name not in curr_df.columns:
        print("No such column exists in the df")
    for key in list_of_keys:
        curr_df[key] = ""
    for i in range(len(curr_df)):
        response_list = eval(curr_df["details"][i])
        if response_list:
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
            columns=mlb.classes_,
        )
    )
    return curr_df


def extract_columns_from_dataframe(df, column_list):
    """provide a dataframe and a column list,
    return the subset of the datafram if the column exists"""
    column_confirmed_list = []
    for column in column_list:
        if column in df.columns:
            column_confirmed_list.append(column)
        else:
            print("{} column not in the dataframe\n".format(column))
    df = df[column_confirmed_list]
    return df


def convert_runtime_to_minutes_int(input_str):
    """
    takes input string eg. `1 hour 10 minutes`
    initialize minutes_int = 0
    Logic: split the string using keyword hour,
    if the length of resulting list is 2:
        Extract 1st item , strip it of white spaces
        and convert it to int and multiply by 60 and
        store in the minutes_int. make the list as
        2nd item only
    split the list on minutes and strip, convert
    it to int and add it to minutes_ans

    return minutes_int"""
    if len(input_str) == 0:
        return None
    keyword_check_list = input_str.split(" ")
    if "hour" in keyword_check_list:
        hour_split_keyword = "hour"
    else:
        hour_split_keyword = "hours"
    if "minutes" in keyword_check_list:
        min_split_keyword = "minutes"
    else:
        min_split_keyword = "minute"
    minutes_ans = 0
    input_list = input_str.split(hour_split_keyword)
    if len(input_list) == 2:
        hour_str = input_list[0]
        hour_str = hour_str.strip()
        hour_int = int(hour_str)
        minutes_ans += 60 * hour_int
        input_str = input_list[1]
        if input_str == "":
            return minutes_ans
    # extract minutes from str
    input_list = input_str.split(min_split_keyword)
    min_str = input_list[0]
    min_str = min_str.strip()
    min_int = int(min_str)
    minutes_ans += min_int

    return minutes_ans


def convert_date_str_to_int_year(input_str):
    resp = re.findall(r"(\d{4})", input_str)
    return resp[0]
