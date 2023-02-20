import hashlib
import pymysql


def get_connection():
    try:
        connection = pymysql.connect(host="sre-bootcamp-selection-challenge.cabf3yhjqvmq.us-east-1.rds.amazonaws.com",
                                     user="secret",
                                     passwd="jOdznoyH6swQB9sTGdLUeeSrtejWkcw",
                                     db="bootcamp_tht")
        return connection
    except pymysql.Error as error:
        print("Database Connection Error: {}".format(error))


def get_user_role_by_token(username):
    query = "SELECT role FROM users WHERE username = %s"
    user_role = ""

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (username,))
        user_role = cursor.fetchone()
    except pymysql.Error as error:
        print("Error retrieving user role from database: {}".format(error))
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

        return user_role


def validateUser(username, password):
    query = "SELECT * FROM users WHERE username = %s"
    result = False

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        hashed_password_from_db = user[1]
        entered_password_by_user = password + user[2]
        entered_hashed_password_by_user = hashlib.sha512(entered_password_by_user.encode()).hexdigest()

        if hashed_password_from_db == entered_hashed_password_by_user:
            result = True

    except pymysql.Error as error:
        print("Error Validating user credentials: {}".format(error))
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

        return result
