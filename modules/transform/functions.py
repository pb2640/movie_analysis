import pandas as pd
import sys

def read_dataframe(path_to_dataframe_with_file_name):
    '''
    Try reading the dataframe. If it fails stop 
    the script and return the error
    
    '''
    try:
        df = pd.read_csv(path_to_dataframe_with_file_name)
    except Exception as e:
        print("There was a problem in reading the file. The following error occured: {}".format(e))
        sys.exit(1)

    return df

