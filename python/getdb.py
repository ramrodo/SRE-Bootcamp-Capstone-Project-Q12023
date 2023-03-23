from mysql.connector import connect, Error

HOST = "sre-bootcamp.czdpg2eovfhn.us-west-1.rds.amazonaws.com"
DATABASE = "bootcamp_tht"
USER = "secret"
PASSWORD = "jOdznoyH6swQB9sTGdLUeeSrtejWkcw"
ENCRYPT_TOKEN = "my2w7wjd7yXF64FIADfJxNs1oupTGAuW"

try:
    conn = connect(host=HOST,
                   database=DATABASE,
                   username=USER,
                   password=PASSWORD,
                   )
    cursor = conn.cursor()

    print("Database connected!")

    # List tables
    query = "SELECT * FROM users"
    cursor.execute(query)
    for (username) in cursor:
        print(username)
    #print(cursor)
    #cursor.close()
    #conn.close()

    # Describe tables
    #query = ("SELECT first_name, last_name, hire_date FROM employees "
    #         "WHERE hire_date BETWEEN %s AND %s")

except Error as error:
    print("Error connecting to Database:", error)
