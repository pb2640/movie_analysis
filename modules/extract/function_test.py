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
    soup = bs(html, "html.parser")
    json_object["details"] = []
    try:
        section_element = soup.find_all("section", {"data-testid": "Details"})
    except Exception as e:
        print("{} exception occured in details section".format(e))
        return json_object
    for div in section_element:
        # Find li elements within the div
        try:
            li_elements = div.find_all("li", attrs={"data-testid": True})

            # Loop through each li element and extract the div text
            for li in li_elements:
                # key name
                try:
                    key_name = li.attrs["data-testid"]
                except Exception as e:
                    print("{} exception occured in details-li section".format(e))
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
        except Exception as e:
            print("{} exception occured in div details section".format(e))

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
    soup = bs(html, "html.parser")
    json_object["boxOffice"] = []
    try:
        section_element = soup.find_all("section", {"data-testid": "BoxOffice"})
    except Exception as e:
        print("{} exception occured".format(e))
        return json_object
    for div in section_element:
        # Find li elements within the div
        try:
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
        except Exception as e:
            print("{} exception occured in boxoffice section".format(e))
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
    soup = bs(html, "html.parser")
    json_object["techspecs"] = []
    try:
        section_element = soup.find_all("section", {"data-testid": "TechSpecs"})
    except Exception as e:
        # print("{} exception occured".format(e))
        return json_object
    for div in section_element:
        try:
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
        except Exception as e:
            pass
            # print("{} exception occured in techspecs section".format(e))
    return json_object


def extract_cast_card_from_html_page(html):
    """
    Take the variable returned by read_html_file and use this function
    to extract information from cast card. If it's successful add the
    extraction to the final json object as a key value pair else print error
    """
    json_object = {}
    json_object["actors"] = []
    soup = bs(html, "html.parser")
    try:
        section_element = soup.find_all("section", {"data-testid": "title-cast"})
    except Exception as e:
        pass
        # print("{} exception occured in cast card".format(e))

    try:
        cast_element = section_element[0].find_all(
            "div", {"data-testid": "title-cast-item"}
        )
        for i in cast_element:
            try:
                img = i.find("img").attrs["src"]
            except Exception as e:
                print("{} exception occured".format(e))
                img = None
            actor_name = i.find("a", {"data-testid": "title-cast-item__actor"}).get_text()
            character_name = i.find(
                "a", {"data-testid": "cast-item-characters-link"}
            ).get_text()
            new_obj = {
                "image": img,
                "actor_name": actor_name,
                "character_name": character_name,
            }
            json_object["actors"].append(new_obj)
    except Exception as e:
        pass
        # print("{} exception occured".format(e))

    try:
        misc_element = section_element[0].find_all(
            "li", {"class": "ipc-metadata-list__item"}
        )
        for i in misc_element:
            lst = []
            if i.find_all(
                "a",
                {
                    "class": "ipc-metadata-list-item__label ipc-metadata-list-item__label--link"
                },
            ):
                key = i.find_all(
                    "a",
                    {
                        "class": "ipc-metadata-list-item__label ipc-metadata-list-item__label--link"
                    },
                )[0].get_text()
            else:
                key = i.find_all(
                    "span",
                    {
                        "class": "ipc-metadata-list-item__label ipc-metadata-list-item__label--btn"
                    },
                )[0].get_text()

            tmp1 = i.find_all("li")
            for j in tmp1:
                if len(j) >= 1:
                    tmp2 = j.find("a").get_text()
                    lst.append(tmp2)
            json_object[key] = lst
    except Exception as e:
        pass
        # print("{} exception occured in cast card".format(e))

    

    

    return json_object


def extract_first_card_from_html_page(html):
    """
    Take the variable returned by read_html_file and use this function
    to extract information from first card. If its successful add the
      extraction to the final
     json object as a key value pair
    else print error
    """
    json_object = {}
    soup = bs(html, "html.parser")
    json_object["first"] = []
    try:
        h1 = soup.find_all("h1")

        json_object["first"].append({"title": h1[0].text})
    except Exception as e:
        pass
        
        # print("{} exception occured in first card in h1".format(e))
    try:
        div_element = soup.find("div", {"data-testid": "hero-media__poster"})
        imgs = div_element.find_all("img")
        for img in imgs:
            json_object["first"].append({"poster_link": img.attrs["src"]})
    except Exception as e:
        pass
        # print("{} exception occured in first card".format(e))

    try:
        div_element = soup.find("div", {"data-testid": "genres"})
        genre_list = []
        all_links = div_element.find_all("a")
        for link in all_links:
            genre_list.append(link.get_text())
        json_object["first"].append({"genres": genre_list})
    except Exception as e:
        pass
        # print("{}exception occured in first card".format(e))
    try:
        p_element = soup.find("p", {"data-testid": "plot"})
        spans = p_element.find_all("span")
        for span in spans:
            json_object["first"].append({"plot": span.get_text()})
            break
    except Exception as e:
        pass
        # print("{} excpetion occured".format(e))
    try:
        div_element = soup.find(
            "div", {"data-testid": "hero-rating-bar__aggregate-rating__score"}
        )
        json_object["first"].append({"imdb-rating": div_element.get_text()})

    except Exception as e:
        pass
        # print("{} excpetion occured".format(e))
    try:
        span_element = soup.find("span", {"class": "score"})
        json_object["first"].append({"metascore": span_element.get_text()})

    except Exception as e:
        pass
        # print("{} excpetion occured".format(e))
    return json_object
