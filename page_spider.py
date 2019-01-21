import os
import argparse
from utils import url_utilities


def main(database: str, url_list_file: str):
    big_word_list = []
    print('We are going to work with ', database)
    print('We are going to scan ', url_list_file)
    urls = url_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        print("Reading " + url)
        page_content = url_utilities.load_page(url=url)
        words = url_utilities.scrape_page(page_contents=page_content)
        big_word_list.extend(words)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite file name")
    parser.add_argument("-i", "--input", help="File of URL's to scan")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)
