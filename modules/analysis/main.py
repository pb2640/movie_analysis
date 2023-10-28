import pandas as pd
from functions import *
import time



if __name__ == "__main__":
    data_path = r"C:\Users\parth\2023\Fall 2023\Projects\docker_hack\data\data.csv"
    # data_path = '/home/server/2023/movies-project-oct/movies_project/data/csv_dumps/data.csv'
    df = pd.read_csv(data_path)
    expanded_df = make_new_columns_boxOffice(df,"boxOffice", ["title-boxoffice-budget","title-boxoffice-cumulativeworldwidegross","title-boxoffice-grossdomestic","title-boxoffice-openingweekenddomestic"])
    expanded_df = make_new_columns_first(expanded_df,'first',['title','poster_link','genres','plot','imdb-rating'])
    expanded_df = make_new_columns_details(expanded_df,"details",['title-details-releasedate','title-details-origin','title-details-languages','title-details-filminglocations','title-details-companies'])
    expanded_df["currency"] = None
    expanded_df["budget_money"] = None
    expanded_df["currency"] = expanded_df["title-boxoffice-budget"].apply(money_str_to_currency)
    expanded_df["budget_money"] = expanded_df["title-boxoffice-budget"].apply(money_str_to_int)
    # create new column num_actors, fills in 0 where no value is present
    expanded_df['num_actors'] = expanded_df['actors'].apply(lambda x: len(eval(x)))
    expanded_df['num_genres'] = expanded_df['genres'].apply(lambda x: len(x))
    expanded_df['imdb_rating'] = expanded_df['imdb-rating'].str.split('/').str[0]
    expanded_df['imdb_rating'] = pd.to_numeric(expanded_df['imdb_rating'], errors='coerce').astype(float)
    expanded_df["runtime"] = None
    expanded_df["soundmix"] = None
    expanded_df["aspect_ratio"] = None
    for i in range(len(expanded_df)):
        input_str = expanded_df["techspecs"][i]
        runtime,soundmix,aspect_ratio = extract_techspecs(input_str)
        expanded_df["runtime"][i] = runtime
        expanded_df["soundmix"][i] = soundmix
        expanded_df["aspect_ratio"][i] = aspect_ratio
    column_list = ['movie_id', 'title-boxoffice-budget', 'title', 'genres', 'plot', 'title-details-releasedate', 'title-details-origin', 
                   'title-details-languages', 'title-details-filminglocations', 'title-details-companies', 'currency', 'budget_money', 
                   'num_actors', 'num_genres', 'imdb_rating', 'runtime', 'soundmix', 'aspect_ratio']

    extract_df = extract_columns_from_dataframe(expanded_df,column_list)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    extract_df.to_csv("../../Data/csvs/{}.csv".format(timestr))
