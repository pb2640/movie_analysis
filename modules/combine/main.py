from function import *
import json

if __name__ == "__main__":
    filepath = '/home/server/2023/movies-project-oct/movies_project/data/json_dumps/tt0000069.json'
    f = open(filepath)
    data = json.load(f)
    # a = normalize_json(filepath)
    for file in filepath:
        a = flatten_data(data)


