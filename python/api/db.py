""" Module for DB connections. """
from mysql.connector import connect, Error

HOST = "sre-bootcamp.czdpg2eovfhn.us-west-1.rds.amazonaws.com"
DATABASE = "bootcamp_tht"
USER = "secret"
PASSWORD = "jOdznoyH6swQB9sTGdLUeeSrtejWkcw"
ENCRYPT_TOKEN = "my2w7wjd7yXF64FIADfJxNs1oupTGAuW"

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
            print("Database connected!")
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
