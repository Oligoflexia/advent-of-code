from dotenv import load_dotenv
import os
import requests

# input: year, day
# output: string
# modifies: creates a .txt file with input-string in /{year}/data/{day}.txt
def get_input(year, day):
    
    input= ""

    url= f"https://adventofcode.com/{str(year)}/day/{str(day)}/input"
    
    load_dotenv()
    cookie = os.getenv('SESSION_COOKIE')
    cookies = {'session': cookie}
    
    headers = {'User-Agent': 'github.com/Oligoflexia/advent-of-code by Oligoflexia'}
    
    data_file_name = str(day) + ".txt"
    data_file_path = os.path.join(str(year), 'data', data_file_name)
    
    if os.path.exists(data_file_path):
        print("Found a datafile!")
        
        with open(data_file_path, "r") as f:
            input = f.read()
    else:
        print("Did not find puzzle input")
        response = requests.get(url, headers=headers, cookies=cookies)
        input = response.text
        print("Creating a datafile!")
    
    with open(data_file_path, "w", newline='') as f:
        f.write(input.rstrip('\n'))
    
    return input

def pprint():
    pass
