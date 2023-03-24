""" Module for DB connections. """
import os
from dotenv import load_dotenv
from mysql.connector import connect, Error

load_dotenv()

HOST = os.environ.get("DB_HOST")
DATABASE = os.environ.get("DB_DATABASE")
USER = os.environ.get("DB_USER")
PASSWORD = os.environ.get("DB_PASSWORD")
ENCRYPT_TOKEN = os.environ.get("JWT_KEY")

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
