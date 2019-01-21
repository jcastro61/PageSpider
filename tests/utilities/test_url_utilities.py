from utilities.url_utilities import load_urls_from_file
from utilities.url_utilities import load_page

def test_load_file():
    test_urls = load_urls_from_file("input.txt")
    assert(len(test_urls) > 1)


def test_load_page():
    html = load_page('https://en.wikipedia.org/wiki/Guido_van_Rossum')
    assert(len(html) > 0)