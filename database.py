import psycopg2
import os
class Database():
    connection = {
        'host': os.getenv('DB_HOST','localhost'),
        'dbname': os.getenv('DB_NAME','stone_challenge'),
        'user': os.getenv('DB_USER','postgres'),
        'password': os.getenv('DB_PASS','masterkey')
    }

    def query(sql):
        try:
            connection = psycopg2.connect(**Database.connection)
            cursor = connection.cursor()
            cursor.execute(sql)
            fields = [ x[0] for x in cursor.description]
            return (fields, cursor.fetchall())
        finally:
            if not connection is None:
                cursor.close()
                connection.close()