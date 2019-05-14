import psycopg2

def deleteInBulk(records):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="117110362",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="rockcontent")
        cursor = connection.cursor()
        ps_delete_query = """Delete from mobile where id = %s"""
        cursor.executemany(ps_delete_query, records)
        connection.commit()
        row_count = cursor.rowcount
        print(row_count, "Record Deleted")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# list of tuples contains database IDs
tuples = [(5, ), (4, ), (3, )]
deleteInBulk(tuples)