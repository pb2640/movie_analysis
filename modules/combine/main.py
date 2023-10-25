from functions import *
import json
import csv
import os
import time

if __name__ == "__main__":
    t0 = time.time()
    data_path = 'data/json_dumps/'
    csv_files_list = os.listdir(data_path)
    csv_files_path = []
    for csv_name in csv_files_list:
        csv_files_path.append(data_path+csv_name)

    headers = ['movie_id', 'first', 'actors', 'details', 'boxOffice', 'techspecs']
    csv_created = False

    with open('data/csv_dumps/data.csv', 'w', newline='') as csv_file:
        csv_created = True
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(headers)

    for csv_file in csv_files_path:
        file_obj = open(csv_file)
        input = json.load(file_obj)
        movie_id = csv_file.split('/')[2].split('.')[0]
        data = [movie_id, input[0]['first'], input[1]['actors'], input[2]['details'], input[3]['boxOffice'], input[4]['techspecs']]
        write_to_csv(data)
    
    t1 = time.time()
    total = t1-t0
    print(f"total time taken is: {total/60} minutes")



