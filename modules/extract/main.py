"""
This file parses the html file
initializes a results array. The result array should contain all result objects
extracts different cards from the imdb page

"""
# file to test performance and correctness of the code
from functions import *
import os
import time
import json
import multiprocessing


def process_html_file(file_path):
    # parse html
    results = []
    write_path = "/home/server/2023/movies-project-oct/movies_project/data/json_dumps/"
    file = read_html_file(file_path)  
    results.append(extract_first_card_from_html_page(file))
    results.append(extract_cast_card_from_html_page(file))
    results.append(extract_details_card_from_html_page(file))
    results.append(extract_boxoffice_card_from_html_page(file))
    results.append(extract_techspecs_card_from_html_page(file))

    # Write the array of objects to a JSON file
    movie_name_new = file_path.split("/movie-")[1].split(".")[0]
    json_file = write_path + movie_name_new + ".json"
    with open(json_file, "w") as json_out:
        json.dump(results, json_out, indent=4)


if __name__ == "__main__":
    t0 = time.time()
    data_path = "/home/server/2023/movies-project-oct/imdb/outputs_18oct/"
    html_files_list = os.listdir(data_path)
    num_files_to_execute = len(html_files_list)
    file_paths = []
    for movie_name in html_files_list[:num_files_to_execute]:
        file_paths.append(data_path + movie_name)
        # process_html_file(data_path + movie_name)
    # Create a pool of worker processes
    # with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust max_workers as needed
    #     executor.map(process_html_file, file_paths)
    with multiprocessing.Pool(processes=10) as pool:
        pool.map(process_html_file, file_paths)

    t1 = time.time()

    total = t1 - t0
    print(
        "Total time taken to execute {} files is : {}".format(
            num_files_to_execute, total / 60
        )
    )


# async def main():
#     data_path = "/home/server/2023/movies-project-oct/imdb/outputs_18oct/"

#     html_files_list = os.listdir(data_path)
#     num_files_to_execute = 10
#     html_files = []
#     for movie_name in html_files_list[:num_files_to_execute]:
#         html_files.append(data_path + movie_name)

#     tasks = [process_html_file(movie_name, html_file) for html_file in html_files]

#     await asyncio.gather(*tasks)

# if __name__ == "__main__":
#     t0 = time.time()
#     asyncio.run(main())


#     t1 = time.time()

#     total = t1-t0
#     print("Total time taken to execute {} files is : {}".format(num_files_to_execute,total/60))
