import urllib.request
from bs4 import BeautifulSoup


def extract_list(url):
    """Takes the URL of a Letterboxd List and converts it to a list of movies
    in python form. List contains tuples of name followed by poster url.
    """

    # Switch to detail view if not already
    if not url.endswith("/detail/"):
        url = url + "detail/"

    web = urllib.request.urlopen(url)
    s = web.read()
    soup = BeautifulSoup(s, 'html.parser')

    # Get the table of films
    film_table = soup.find(class_="film-list")

    # Need to extract the poster url and title of each film
    for row in film_table.find_all(class_="film-detail"):
        poster_url = row.div.find(class_="image")["src"]
        name = row.find(class_="film-detail-content").h2.a.string

        yield (name, poster_url)


def names_list(url):
    """Returns just movie names"""

    return map(lambda film: film[0], extract_list(url))


if __name__ == "__main__":
    films = extract_list("https://letterboxd.com/monstervision/list/mad-max-rip-offs-maxsploitation/detail/")
    for film in films:
        print(film)
