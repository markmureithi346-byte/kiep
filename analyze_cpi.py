from database import get_connection, execute_query, close_connection

MAIN_QUERY = """
SELECT month, cpi_index, yearly_inflation
FROM cpi_monthly
ORDER BY month;
"""

conn = get_connection()
rows = execute_query(conn, MAIN_QUERY)
close_connection(conn)

for row in rows:
    print(row)
    