from database import get_connection, close_connection

connection = get_connection()

close_connection(connection)