import pandas as pd
from functions import *


data_path = r"C:\Users\parth\2023\Fall 2023\Projects\docker_hack\data\data.csv"


#read the data
df = pd.read_csv(data_path)


new_df = df
new_df = make_new_columns_boxOffice(new_df,"boxOffice", ["title-boxoffice-budget","title-boxoffice-cumulativeworldwidegross","title-boxoffice-grossdomestic","title-boxoffice-openingweekenddomestic"])
new_df = make_new_columns_first(new_df,'first',['title','poster_link','genres','plot','imdb-rating'])
new_df.drop(['first','boxOffice','poster_link'], axis = 1, inplace = True)
# pre-processing steps

# capture only the imdb rating, remove /10 part and convert to float, insert NaN where no value exists
new_df['imdb_rating'] = new_df['imdb-rating'].str.split('/').str[0]
new_df['imdb_rating'] = pd.to_numeric(new_df['imdb_rating'], errors='coerce').astype(float)

# create new column #genres, fills in 0 where no value is present
new_df['num_genres'] = new_df['genres'].apply(lambda x: len(x))

# create new column #actors, fills in 0 where no value is present
new_df['num_actors'] = new_df['actors'].apply(lambda x: len(eval(x)))

new_df["currency"] = None
new_df["budget_money"] = None

new_df["currency"] = new_df["title-boxoffice-budget"].apply(money_str_to_currency)
new_df["budget_money"] = new_df["title-boxoffice-budget"].apply(money_str_to_int)

new_df["runtime"] = None
new_df["soundmix"] = None
new_df["aspect_ratio"] = None
for i in range(len(new_df)):
    input_str = new_df["techspecs"][i]
    runtime,soundmix,aspect_ratio = extract_techspecs(input_str)
    new_df["runtime"][i] = runtime
    new_df["soundmix"][i] = soundmix
    new_df["aspect_ratio"][i] = aspect_ratio
    