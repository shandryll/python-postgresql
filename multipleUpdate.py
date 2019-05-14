import psycopg2

def updateInBulk(records):
    try:
        connection = psycopg2.connect(user="postgres",
                                         password="117110362",
                                         host="127.0.0.1",
                                         port="5432",
                                         database="rockcontent")
        cursor = connection.cursor()
        # Update multiple records
        sql_update_query = """Update mobile set price = %s where id = %s"""
        cursor.executemany(sql_update_query, records)
        connection.commit()
        row_count = cursor.rowcount
        print(row_count, "Records Updated")

    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

tuples = [(750, 4), (950, 5)]
updateInBulk(tuples)