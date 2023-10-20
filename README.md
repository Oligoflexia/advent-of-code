# Soup's Advent of Code Solutions
A **WIP** repository of solutions to the yearly Advent of Code puzzles.
Solutions are primarily created for learning purposes and do not guarantee optimal efficiency, correctness or **safety**.

<br>

I have greatly enjoy the puzzles so far, and would highly recommend them to everyone,
regardless of programming or CS expertise. Check it out at [adventofcode.com](https://adventofcode.com)!

<br>
<br>

## Running solutions on your own machine

#### WIP

<br>
<br>

## A note on automation
This application tries to maintain best practices for requests to AoC servers as per the 
[Automation FAQ - Reddit](https://www.reddit.com/r/adventofcode/wiki/faqs/automation). 

<br>

The only request to the AoC API is made in the `get_input()` method in `utils/get_input.py`. 
This function takes a year and date input and uses them to construct a URI in order to
request the user input string. The user input string is then cached locally in `{year}/data/`.  
This automated process was set up in order to avoid errors caused by `\n` characters and
to make the solution scripts easier to look at.

<br>

In order to ensure that AoC servers aren't pinged unnecessarily, `get_input()` first looks at 
`{year}/data` to verify if a file with the input already exists. If it does, that
local file is read into the script. The only time an external request is made is if the 
input does not exist locally. Thus, requests are constrained to a single inital request to
download the input, and only ever again for the same input if it is deleted by the user.

<br>

In addition, the `User-Agent` string in the header of the get request has been edited with
a link back to this repo for better visibility.

<br>

Relevant code snippets highlighting the above measures are provided below:

    import requests

    def get_input(year, day):

build URI:

        url= f"https://adventofcode.com/{str(year)}/day/{str(day)}/input"

create dict for cookies and header:

        cookies = {'session': cookie}

        headers = {'User-Agent': 'github.com/Oligoflexia/advent-of-code by Oligoflexia'}

only make API call if input not cached:

        if os.path.exists(data_file_path):
            print("Found a datafile!")
            ...
        else:
            print("Did not find puzzle input")

add helpful header information to request:

            response = requests.get(url, header=headers, cookies=cookies)

        
cache input locally to avoid having to make further calls:

        with open(data_file_path, "w", newline='') as f:
            f.write(input.rstrip('\n'))

<br>
<br>

## A note on personalized user inputs
The cached user input files I used are unavailable in this repo due to the proper handling measures
outlined in [Inputs FAQ - Reddit](https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs). 

<br>

The solution scripts can be run on your machine by (either): 

1. creating a `.env` file in your root directory containing your user session cookie `SESSION_COOKIE=`
2. downloading your own unique user inputs and placing them in the appropriate `{year}/data/`
folder.
    - the input file is named `{day}.txt`, where day is an int corresponding to the puzzle day.

