from mysql.connector import connect, Error, errorcode

HOST = "capstone-db-public.crupwggs3ofp.us-west-2.rds.amazonaws.com"
DATABASE = "capstone_db_public"
USER = "admin"
PASSWORD = "mwn0cbq6rxw0MHM*zrc"
ENCRYPT_TOKEN = "my2w7wjd7yXF64FIADfJxNs1oupTGAuW"

try:
    conn = connect(host=HOST,
            database=DATABASE,
            username=USER,
            password=PASSWORD,
            )
    cursor = conn.cursor()

    #print("Database connected!")

    # Delete table

    # query_delete_db = "DROP TABLE users"
    # cursor.execute(query_delete_db)
    # conn.commit()

    # Delete data

    # query_delete = "DELETE FROM users WHERE username='admin'"
    # cursor.execute(query_delete)
    # conn.commit()

    # Create tables

    TABLES = {}
    TABLES['users'] = (
        "CREATE TABLE `users` ("
        "  `username` VARCHAR(20),"
        "  `password` VARCHAR(400),"
        "  `salt` VARCHAR(20),"
        "  `role` VARCHAR(20),"
        "  PRIMARY KEY (`username`)"
        ") ")

    for table_name, table_description in TABLES.items():
        try:
            print(f"Creating table {table_name}...")
            cursor.execute(table_description)
        except Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f"table '{table_name}' already exists.")
            else:
                print(err.msg)
        else:
            print("OK")


    #Insert data

    add_admin = ("INSERT INTO users "
                    "(username, password, salt, role) "
                    "VALUES (%s, %s, %s, %s)")

    data_admin = ('admin',
                  '15e24a16abfc4eef5faeb806e903f78b188c30e4984a03be4c243312f198d1229ae8759e98993464cf713e3683e891fb3f04fbda9cc40f20a07a58ff4bb00788',
                  'F^S%QljSfV',
                  'admin')

    add_bob = ("INSERT INTO users "
                "(username, password, salt, role) "
                "VALUES (%s, %s, %s, %s)")

    data_bob = ('bob',
                '2c9dab627bd73b6c4be5612ff77f18fa69fa7c2a71ecedb45dcec45311bea736e320462c6e8bfb2421ed112cfe54fac3eb9ff464f3904fe7cc915396b3df36f0',
                'F^S%QljSfV',
                'viewer')

    add_noadmin = ("INSERT INTO users "
               "(username, password, salt, role) "
               "VALUES (%s, %s, %s, %s)")

    data_noadmin = ('noadmin',
                    '89155af89e8a34dcbde088c72c3f001ac53486fcdb3946b1ed3fde8744ac397d99bf6f44e005af6f6944a1f7ed6bd0e2dd09b8ea3bcfd3e8862878d1709712e5',
                    'KjvFUC#K*i',
                    'editor')

    cursor.execute(add_admin, data_admin)
    cursor.execute(add_bob, data_bob)
    cursor.execute(add_noadmin, data_noadmin)
    conn.commit()

    # Query data
    query = "SELECT * FROM users"
    cursor.execute(query)
    for (row) in cursor:
        print(row)

    # Close connection

    cursor.close()
    conn.close()

except Error as error:
    print("Error connecting to Database:", error)
