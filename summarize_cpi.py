from database import get_connection, execute_query, close_connection
import pandas as pd

conn = get_connection()
rows = execute_query(conn, "SELECT month, cpi_index, Yearly_inflation FROM cpi_monthly ORDER BY month;")
close_connection(conn)

df = pd.DataFrame(rows, columns=["month", "cpi_index", "Yearly_inflation"])
print("CPI DATA")
print(df)
print()
print("SUMMARY")
print("Average yearly inflation", round(df["Yearly_inflation"].mean(), 2))
print("Highest inflation month :", df.loc[df["Yearly_inflation"].idxmax(), "month"])
print("largest CPI index          :", df["cpi_index"].iloc[-1])
