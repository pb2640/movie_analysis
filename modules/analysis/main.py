import pandas as pd
from functions import *
import time
import cpi


if __name__ == "__main__":
    data_path = r"C:\Users\parth\2023\Fall 2023\Projects\docker_hack\data\data.csv"
    # data_path = '/home/server/2023/movies-project-oct/movies_project/data/csv_dumps/data.csv'
    df = pd.read_csv(data_path)
    expanded_df = make_new_columns_boxOffice(
        df,
        "boxOffice",
        [
            "title-boxoffice-budget",
            "title-boxoffice-cumulativeworldwidegross",
            "title-boxoffice-grossdomestic",
            "title-boxoffice-openingweekenddomestic",
        ],
    )
    expanded_df = make_new_columns_first(
        expanded_df, "first", ["title", "poster_link", "genres", "plot", "imdb-rating"]
    )
    expanded_df = make_new_columns_details(
        expanded_df,
        "details",
        [
            "title-details-releasedate",
            "title-details-origin",
            "title-details-languages",
            "title-details-filminglocations",
            "title-details-companies",
        ],
    )
    expanded_df["currency"] = None
    expanded_df["budget_money"] = None
    # delete commas in the budget str
    expanded_df["title-boxoffice-budget"] = expanded_df[
        "title-boxoffice-budget"
    ].str.replace(",", "")
    # extract currency
    expanded_df["currency"] = expanded_df["title-boxoffice-budget"].str.extract(
        r"(^\D+)"
    )
    # extract money int
    expanded_df["budget_money"] = expanded_df["title-boxoffice-budget"].str.extract(
        r"(\d+)"
    )
    # convert int type of budget money to int
    expanded_df["budget_money"] = pd.to_numeric(
        expanded_df["budget_money"], errors="coerce"
    ).astype("Int64")
    # create new column num_actors, fills in 0 where no value is present
    expanded_df["num_actors"] = expanded_df["actors"].apply(lambda x: len(eval(x)))
    expanded_df["num_genres"] = expanded_df["genres"].apply(lambda x: len(x))
    expanded_df["imdb_rating"] = expanded_df["imdb-rating"].str.split("/").str[0]
    expanded_df["imdb_rating"] = pd.to_numeric(
        expanded_df["imdb_rating"], errors="coerce"
    ).astype(float)
    expanded_df["runtime"] = None
    expanded_df["soundmix"] = None
    expanded_df["aspect_ratio"] = None
    for i in range(len(expanded_df)):
        input_str = expanded_df["techspecs"][i]
        runtime, soundmix, aspect_ratio = extract_techspecs(input_str)
        expanded_df["runtime"][i] = runtime
        expanded_df["soundmix"][i] = soundmix
        expanded_df["aspect_ratio"][i] = aspect_ratio
    column_list = [
        "movie_id",
        "title-boxoffice-budget",
        "title",
        "genres",
        "plot",
        "title-details-releasedate",
        "title-details-origin",
        "title-details-languages",
        "title-details-filminglocations",
        "title-details-companies",
        "currency",
        "budget_money",
        "num_actors",
        "num_genres",
        "imdb_rating",
        "runtime",
        "soundmix",
        "aspect_ratio",
    ]

    extract_df = extract_columns_from_dataframe(expanded_df, column_list)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    extract_df.to_csv("../../Data/csvs/{}.csv".format(timestr))

    df_v2 = extract_df.drop(['movie_id','title','plot','title','title-details-filminglocations','title-details-companies','num_genres', 'imdb_rating', 'soundmix', 'aspect_ratio', 'title-boxoffice-budget'],axis = 1)
    df_v2 = df_v2.dropna()
    df_v2 = df_v2[df_v2['currency']=='$']
    df_v2 = df_v2[df_v2['title-details-languages']!='[\'None\']']
    df_v2 = df_v2.reset_index(drop=True)
    none_lang_ind = []
    for i in range(len(df_v2)):
        if 'None' in df['title-details-languages'][i]:
            none_lang_ind.append(i)
    df_v2 = df_v2.drop(index=none_lang_ind,axis=1)
    common_langs = ['[\'English\']','[\'French\']','[\'Spanish\']','[\'German\']','[\'Arabic\']','[\'Hindi\']','[\'Italian\']','[\'Chinese\']','[\'Mandarin\']','[\'Russian\']', '[\'Latin\']', '[\'Japanese\']', '[\'Persian\']', '[\'Bengali\']']
    df_v2 = df_v2[df_v2['title-details-languages'].isin(common_langs)]
    df_v2 = df_v2.reset_index(drop=True)

    df_v2['genres'] = df_v2['genres'].astype(str)
    df_v2['title-details-releasedate'] = df_v2['title-details-releasedate'].astype(str)
    df_v2['title-details-origin'] = df_v2['title-details-origin'].astype(str)
    df_v2['title-details-languages'] = df_v2['title-details-languages'].astype(str)
    df_v2['runtime'] = df_v2['runtime'].astype(str)

    df_v2['genres'] = df_v2['genres'].apply(lambda x: eval(x))
    df_v2['title-details-languages'] = df_v2['title-details-languages'].apply(lambda x: eval(x))
    df_v2 = encode_variable(df_v2,'genres')
    df_v2 = encode_variable(df_v2, 'title-details-languages')
    df_v2['release_year'] = df_v2['title-details-releasedate'].str.extract(r'(\d{4})').astype('category')
    df_v2 = df_v2.drop(['genres','title-details-languages','title-details-origin','title-details-releasedate'],axis=1)

    df_v2['runtime'] = df_v2['runtime'].apply(lambda x: convert_runtime_to_minutes_int(x))

    # filter for movies b/w 2008 and 2022 (since cpi package works till 2021)
    df_v2 = df_v2[(df_v2['release_year'].astype('int')>2008) & (df_v2['release_year'].astype('int')<2022)]
    # create a new column 'budget_adjusted', which contains the budget amount adjusted for inflation in 2021
    for i in range(len(df_v2)):
        df_v2['budget_adjusted'][i] = cpi.inflate(df_v2['budget_money'][i],df_v2['release_year'][i],to=2021)
