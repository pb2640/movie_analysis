import pandas as pd
from functions import Model, ProcessDataframe


if __name__ == "__main__":
    #process dataframe
    data_path = r"C:\Users\parth\2023\Fall 2023\Projects\movie_analysis\data\csvs\data2.csv"
    df = ProcessDataframe(data_path)
    df.remove_columns(["release_year","runtime_int","num_actors","budget_money","title-details-companies"])
    df.remove_na_rows(["budget_money","runtime_int"])
    df.reduce_categorical_variables_dimensions("title-details-companies",10)
    prepared_df = df.encode_variable("title-details-companies")

    print(prepared_df.head())
    model = Model(prepared_df, "budget_money", "regression")
    model.prepare_train_test_datasets()
    model.train_model()
    model.test_model()
    model.report_model_results()


    print("Done")
