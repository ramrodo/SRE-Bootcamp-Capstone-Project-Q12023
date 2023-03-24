""" Methods for login module. """
import hashlib
import jwt
from mysql.connector import Error
from api.db import Database

class Token:
    """ Class to handle the token for authentication. """

    def generate_token(self, username, password):
        """ Generates a JWT token with the data given. """
        try:
            db_conn = Database()
        except Error as error:
            print("Error connecting to Database:", error)

        query_data = db_conn.get_user(username)
        query_password_hashed = query_data[1]
        query_salt = query_data[2]
        query_role = query_data[3]

        if username is not None and password is not None:
            hashed_password = hashlib.sha512(
                (password + query_salt).encode("utf-8")).hexdigest()

            if query_password_hashed == hashed_password:
                payload = { "role": query_role }
                jwt_token = jwt.encode(
                    payload,
                    db_conn.get_encrypt_token(),
                    algorithm="HS256",
                )
                return jwt_token

            return False

        return False

class Restricted:
    """ Class to handle the protected data. """

    def access_data(self, authorization):
        """ Verifies and authorize the access to the data. """
        if authorization:
            try:
                bearer_token = authorization.replace("Bearer", "").strip()

                db_conn = Database()

                data_decoded = jwt.decode(
                    bearer_token,
                    db_conn.get_encrypt_token(),
                    algorithms=["HS256"],
                )
            except jwt.ExpiredSignatureError as expired_signature_error:
                return expired_signature_error
            except jwt.DecodeError as decode_error:
                return decode_error

            if "role" in data_decoded:
                return "You are under protected data"

        return ""
