'''import pandas as pd
from bs4 import BeautifulSoup as bs4
import requests 

url = "https://letterboxd.com/dessie_/list/every-movie-posted-on-the-asian-cinema-archive/"

page = requests.get(url)
soup = bs4(page.text, 'html.parser')
dfs = pd.read_html(page.text)
film = soup.find_all("div", class_="div.react-component.poster.film-poster")

for index, film in enumerate(film):
    title = film['data-film-name']
    film_url = film['data-film-link']
    poster_url = film['data-poster-url']
   print(f"Title: {title}, URL: {film_url}, poster: {poster_url}")


## info from the topic
# data from April 2025 '''

'''import requests
from bs4 import BeautifulSoup  
import pandas as pd

url = "https://letterboxd.com/dessie_/list/every-movie-posted-on-the-asian-cinema-archive/" #link 
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')  # Correct initialization
#dfs = pd.read_html(page.text)

# Use the correct selector syntax
# Option 1: Use find_all with just the class name
#films = soup.find_all("div", class_="film-poster")  # Just use the class name
films = soup.find_all("div", "class=js-list-entries poster-list -p125 -grid")
# use CSS selector with select() method if you need complex selection


for index, film in enumerate(films):
    # Use get() method to safely access attributes
    title = film.get('data-film-name', 'No title')
    film_url = film.get('data-film-link', 'No URL')
    poster_url = film.get('data-film-poster-url', 'No poster')  # Note: I fixed this attribute name as a guess
    print(f"Title: {title}, URL: {film_url}, poster: {poster_url}")

    '''

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://letterboxd.com/dessie_/list/every-movie-posted-on-the-asian-cinema-archive/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Option 1: Using class_ parameter (remove 'div.' prefix)
films = soup.find_all("li", class_="posteritem")

# Option 2: Using CSS selector with select()
#films = soup.select("li.posteritem")



for index, film in enumerate(films):
    film_url = film.get('data-film-link', 'No URL')
    poster_url = film.get('data-film-poster-url', 'No poster')
    print(f"{index + 1}. Title: {title}, URL: {film_url}, Poster: {poster_url}")

    