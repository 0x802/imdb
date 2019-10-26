#!/usr/bin/python3
try:
    import requests
except ImportError:
    print("error import 'requests' model ")
    exit()

try:
    import click  
except ImportError:
    print("error import 'click' model ")
    exit()

try:
    import json
except ImportError:
    print("error import 'json' model ")
    exit()

try:
    from interruptingcow import timeout
except ImportError:
    print("error import 'interruptingcow' model ")
    exit()


KEY = 'ab0b60cf' # this is my API KEY

# Color 
G = '\033[1;32m'
T = '\033[1;33m'
N = '\033[0m'

# Start Codes
def get_information(*args, **kwargs):
    title, year = args
    try:
        with timeout(20):
            print(f'{G}Searching in Imdb Database....{N}')
            return requests.get(f'http://www.omdbapi.com/?t={title}&y={year}&apikey={KEY}').text
    except RuntimeError:
        print("[!]Time Out!")


def filters(*args, **kwargs):
    try:
        DATA = json.loads(get_information(args[0], args[1]))
        print(f"Title:      {T}{DATA['Title']}{N}")
        print(f"Year:       {T}{DATA['Year']}{N}")
        print(f"Rated:      {T}{DATA['Rated']}{N}")
        print(f"Released:   {T}{DATA['Released']}{N}")
        print(f"Runtime:    {T}{DATA['Runtime']}{N}")
        print(f"Genre:      {T}{DATA['Genre']}{N}")
        print(f"Actors:     {T}{DATA['Actors']}{N}")
        print(f"Language:   {T}{DATA['Language']}{N}")
        print(f"Country:    {T}{DATA['Country']}{N}")
        print(f"Imageurl:   {T}{DATA['Poster']}{N}")
        print(f"Star:       {T}{DATA['imdbRating']}{N}")
        print(f"imdbVotes:  {T}{DATA['imdbVotes']}{N}")

    except Exception as e:
        print(f'[!]Not Find The Move! or {e}')

# Options
@click.command()
@click.option('-t','--title',help='Title The Move.')
@click.option('-y', '--year', type=click.STRING, help='The Year move in run')
@click.help_option(help='For the assistant')
def main(title, year):
    """Imdb Database"""
    try:
        filters(title.replace(' ', '+'), year if year != '' else '2019')
    except AttributeError:
        print("[!]No Find title")

# run script
if __name__ == "__main__":
    main()
