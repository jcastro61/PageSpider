import sqlite3 as lite


def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists words")
        ddl = "CREATE TABLE 'words' ( 'word' TEXT NOT NULL, 'usage_count' INTEGER NOT NULL DEFAULT 1, PRIMARY KEY('word'))"
        cur.execute(ddl)
        ddl = "CREATE UNIQUE INDEX words_idx on words(word)"
        cur.execute(ddl)
    conn.close()


def save_words_to_database(database_path: str, word_list: list):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        for word in word_list:
            if word == 'the' or word == 'and' or word == 'of' or word == 'to':
                continue
            sql = "select count(*) from words where word = '" + word + "'"
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count +1 where word ='" + word + "'"
            else:
                sql = "INSERT into words(word) values ( '" + word + "')"
            cur.execute(sql)
    conn.close()
    print("Database save completed")
