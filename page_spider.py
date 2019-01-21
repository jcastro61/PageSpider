import os
import argparse
from utilities import url_utilities
from utilities import database_utilities


def main(database: str, url_list_file: str):
    big_word_list = []
    print('We are going to work with ', database)
    database_utilities.create_database(database_path=database)
    print('We are going to scan ', url_list_file)
    urls = url_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        print("Reading " + url)
        page_content = url_utilities.load_page(url=url)
        words = url_utilities.scrape_page(page_contents=page_content)
        big_word_list.extend(words)

    os.chdir(os.path.dirname(__file__))
    path = os.path.join(os.getcwd(), database)
    database_utilities.save_words_to_database(database_path=path, word_list=big_word_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite file name")
    parser.add_argument("-i", "--input", help="File of URL's to scan")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)