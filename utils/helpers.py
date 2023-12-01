from dotenv import load_dotenv
import os
import requests


def get_input(day: int, year: int):
    """
    input: year, day
    output: string
    modifies: creates a .txt file with input-string in /{year}/data/{day}.txt
    """
    str_input = ""

    url = f"https://adventofcode.com/{str(year)}/day/{str(day)}/input"

    load_dotenv()
    cookie = os.getenv("SESSION_COOKIE")
    cookies = {"session": cookie}

    headers = {
        "User-Agent": "github.com/Oligoflexia/advent-of-code by Oligoflexia"
    }

    data_file_name = str(day) + ".txt"
    data_file_path = os.path.join(str(year), "data", data_file_name)

    if os.path.exists(data_file_path):
        print("Found a datafile!")

        with open(data_file_path, "r") as f:
            str_input = f.read()
    else:
        print("Did not find puzzle input")
        response = requests.get(url, headers=headers, cookies=cookies)
        str_input = response.text
        print("Creating a datafile!")

    with open(data_file_path, "w", newline="") as f:
        f.write(str_input.rstrip("\n"))

    return str_input


def pprint():
    pass
