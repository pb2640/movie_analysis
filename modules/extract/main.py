'''
This file parses the html file
initializes a results array. The result array should contain all result objects
extracts different cards from the imdb page

'''
from functions import *

data_path = "/home/server/2023/movies-project-oct/imdb/outputs_18oct/"

movie_name = "movie-tt0496806.html"
file_path = data_path + movie_name
# parse html

file = read_html_file(file_path)
results = []
results.append(extract_details_card_from_html_page(file))
results.append(extract_boxoffice_card_from_html_page(file))
results.append(extract_techspecs_card_from_html_page(file))
print("done")
