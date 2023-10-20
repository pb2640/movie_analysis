"""
This script contains all functions

The following guidelines must be implemented for best practices:

-> Include Comment after declaring a function, this will act as
docstring when this functions is called
-> Run Flake8 after every commit
-> Run black after every commit

TODO : Log errors

"""
import sys
from bs4 import BeautifulSoup as bs


# reads the html file and stores it in a variable
def read_html_file(path):
    """
    Takes the path name with file as input and returns a variable
    with parsed text
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print("There was an error reading the file :{}".format(e))
        sys.exit(1)
    return text


def extract_details_card_from_html_page(html):
    """
    Take the variable returned by read_html_file and use this function
    to extract information from details card. If its successful add the
      extraction to the final
     json object as a key value pair
    else print error
    """
    json_object = {}
    soup = bs(html)
    section_element = soup.find_all("section", {"data-testid": "Details"})
    json_object["details"] = []
    for div in section_element:
        # Find li elements within the div
        li_elements = div.find_all("li", attrs={"data-testid": True})

        # Loop through each li element and extract the div text
        for li in li_elements:
            # key name
            key_name = li.attrs["data-testid"]

            # Find all li elements within the ul
            div_elements = li.find_all("div")

            # Loop through each li element within the ul
            for div in div_elements:
                # Extract the text from the li element
                # div_text = div.get_text()
                a_arr = []
                a_tags = div.find_all("a")
                a_href_arr = []
                for a in a_tags:
                    a_arr.append(a.get_text())
                    try:
                        a_href_arr.append(a.attrs["href"])
                    except Exception as e:
                        print(
                            """No links for this a tag,
                              following error occured {}""".format(
                                e
                            )
                        )
                        a_href_arr.append["None"]
                        pass
                # find all links and append the text to the list
                new_obj = {key_name: {"val": a_arr, "link": a_href_arr}}
                json_object["details"].append(new_obj)

    return json_object


def extract_boxoffice_card_from_html_page(html):
    """
    Take the variable returned by read_html_file and use this function
    to extract information from boxofficecard card. If its successful add the
      extraction to the final
     json object as a key value pair
    else print error
    """
    json_object = {}
    soup = bs(html)
    section_element = soup.find_all("section", {"data-testid": "BoxOffice"})
    json_object["boxOffice"] = []
    for div in section_element:
        # Find li elements within the div
        li_elements = div.find_all("li", attrs={"data-testid": True})

        # Loop through each li element and extract the div text
        for li in li_elements:
            # key name
            key_name = li.attrs["data-testid"]

            # Find all li elements within the ul
            span_elements = li.find_all(
                "span", {"class": "ipc-metadata-list-item__list-content-item"}
            )

            # Loop through each li element within the ul
            for span in span_elements:
                # Extract the text from the li element
                span_text = span.get_text()
                new_obj = {key_name: {"val": span_text}}
                json_object["boxOffice"].append(new_obj)

    return json_object


def extract_techspecs_card_from_html_page(html):
    """
    Take the variable returned by read_html_file and use this function
    to extract information from technical specs card. If its successful add the
      extraction to the final
     json object as a key value pair
    else print error
    """
    json_object = {}
    soup = bs(html)
    section_element = soup.find_all("section", {"data-testid": "TechSpecs"})
    json_object["techspecs"] = []
    for div in section_element:
        # Find li elements within the div
        li_elements = div.find_all("li", attrs={"data-testid": True})

        # Loop through each li element and extract the div text
        for li in li_elements:
            # key name
            key_name = li.attrs["data-testid"]
            # Find all li elements within the ul
            div_elements = li.find_all(
                "div", {"class": "ipc-metadata-list-item__content-container"}
            )
            # Loop through each li element within the ul
            for div in div_elements:
                # Extract the text from the li element
                # store multiple responses for a key in an array
                if key_name == "title-techspec_runtime":
                    new_obj = {key_name: {"val": div.get_text()}}
                    json_object["techspecs"].append(new_obj)
                    continue
                li_arr = []
                all_lis = div.find_all("li")
                for temp_li in all_lis:
                    li_arr.append(temp_li.get_text())
                # div_text = div.get_text()
                new_obj = {key_name: {"val": li_arr}}
                json_object["techspecs"].append(new_obj)

    return json_object
