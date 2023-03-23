""" Module for DB connections. """
from mysql.connector import connect, Error

HOST = "capstone-db-public.crupwggs3ofp.us-west-2.rds.amazonaws.com"
DATABASE = "capstone_db_public"
USER = "admin"
PASSWORD = "mwn0cbq6rxw0MHM*zrc"
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
