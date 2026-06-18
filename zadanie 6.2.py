import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

def add_genre(conn, genre):
   """
   Create a new genre into the genres table
   :param conn:
   :param genre:
   :return: project id
   """
   sql = '''INSERT INTO genres(genre, quantity)
             VALUES(?,?)'''
   cur = conn.cursor()
   cur.execute(sql, genre)
   conn.commit()
   return cur.lastrowid

def add_game(conn, game):
   """
   Create a new game into the games table
   :param conn:
   :param game:
   :return: task id
   """
   sql = '''INSERT INTO games(genre_id, name, score)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, game)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":

   create_genres_sql = """
   -- genres table
   CREATE TABLE IF NOT EXISTS genres (
      id integer PRIMARY KEY,
      genre text NOT NULL,
      quantity integer
   );
   """

   create_games_sql = """
   -- games table
   CREATE TABLE IF NOT EXISTS games (
      id integer PRIMARY KEY,
      genre_id integer NOT NULL,
      name VARCHAR(50) NOT NULL,
      score integer
   );
   """

   db_file = "games.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_genres_sql)
       execute_sql(conn, create_games_sql)
       conn.close()

   genre = ("FPS", 100)
   genre1 = ('RPG', 150)
   genre2 = ('Strategy', 27)

   conn = create_connection("games.db")
   pr_id = add_genre(conn, genre)
   pr_id1 = add_genre(conn, genre1)
   pr_id2 = add_genre(conn, genre2)

   game = (pr_id,"BF 6",8)
   game1 = (pr_id,"WW3",9)
   game2 = (pr_id1, 'BG 3', 10)
   
   game_id = add_game(conn, game)
   game_id1 = add_game(conn, game1)
   game_id2 = add_game(conn, game2)

   
   conn.commit()

   



   