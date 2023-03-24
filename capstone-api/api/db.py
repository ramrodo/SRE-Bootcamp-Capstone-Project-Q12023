""" Module for DB connections. """
from dotenv import dotenv_values
from mysql.connector import connect, Error

config = dotenv_values(".env")

HOST = config["DB_HOST"]
DATABASE = config["DB_DATABASE"]
USER = config["DB_USER"]
PASSWORD = config["DB_PASSWORD"]
ENCRYPT_TOKEN = config["JWT_KEY"]

class Database():
    """ Methods to interact with the Database. """

    def __init__(self):
        try:
            self.conn = connect(host=HOST,
                                database=DATABASE,
                                username=USER,
                                password=PASSWORD,
            )
            self.cursor = self.conn.cursor()
            self.encrypt_token = ENCRYPT_TOKEN
        except Error as error:
            print("Error connecting to Database:", error)


    def get_user(self, username):
        """ Get data from the Database of the user given. """
        query = f"SELECT * FROM users WHERE username='{username}' LIMIT 1"
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def get_encrypt_token(self):
        """ Returns the encrypted token. """
        return self.encrypt_token
