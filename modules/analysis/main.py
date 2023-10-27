"""
This file parses the html file
initializes a results array. The result array should contain all result objects
extracts different cards from the imdb page

"""
from functions import *
import pandas as pd


if __name__ == "__main__":
    data_path = '/home/server/2023/movies-project-oct/movies_project/data/csv_dumps/data.csv'
    df = pd.read_csv(data_path)
    expanded_df = make_new_columns_boxOffice(df,"boxOffice", ["title-boxoffice-budget","title-boxoffice-cumulativeworldwidegross","title-boxoffice-grossdomestic","title-boxoffice-openingweekenddomestic"])
    expanded_df = make_new_columns_first(expanded_df,'first',['title','poster_link','genres','plot','imdb-rating'])
    expanded_df = make_new_columns_details(expanded_df,"details",['title-details-releasedate','title-details-origin','title-details-languages','title-details-filminglocations','title-details-companies'])
    
    # create new column #actors, fills in 0 where no value is present
    expanded_df['num_actors'] = expanded_df['actors'].apply(lambda x: len(eval(x)))

    # Capture only the imdb rating, remove /10 part and convert to float, insert NaN where no value exists
    expanded_df['imdb_rating'] = expanded_df['imdb-rating'].str.split('/').str[0]
    expanded_df['imdb_rating'] = pd.to_numeric(expanded_df['imdb_rating'], errors='coerce').astype(float)

    # unpack genres column into encoded
    expanded_df = encode_variable(expanded_df, 'genres')

    # Drop all unexpanded and unnecessary columns
    # new_df.drop(['first','boxOffice','poster_link','actors','details'], axis = 1, inplace = True)