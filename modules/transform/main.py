import pandas as pd
from functions import read_dataframe
import time

transform_data_path  = r"C:\Users\parth\2023\Fall 2023\Projects\movie_analysis\data\csvs\data.csv"


if __name__ == "__main__":
    df = read_dataframe(transform_data_path)
    