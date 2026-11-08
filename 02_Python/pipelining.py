
import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

# ==========================================
# 1. SQL SERVER CONNECTION
# ==========================================

connection_string = quote_plus(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=LAPTOP-4ND7RR1H\\SQLEXPRESS;"
    "DATABASE=Netflix;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={connection_string}"
)

print("SQL Server connection created!")


# ==========================================
# 2. READ CLEANED CSV FILE
# ==========================================

file_path = r"C:\Users\sneha\OneDrive\Desktop\Netflix Final project\Netflix_Clean_Data.csv"

df = pd.read_csv(file_path)

print("\nData Preview:")
print(df.head())

print("\nData Shape:")
print(df.shape)


# ==========================================
# 3. CHECK SQL SERVER CONNECTION
# ==========================================

with engine.connect() as connection:

    result = connection.execute(
        text("""
            SELECT
                @@SERVERNAME AS Server_Name,
                DB_NAME() AS Database_Name
        """)
    )

    print("\nSQL Server Details:")
    print(result.fetchone())


# ==========================================
# 4. LOAD DATA INTO SQL SERVER
# ==========================================

df.to_sql(
    name="Netflix_Customers",
    con=engine,
    schema="dbo",
    if_exists="replace",
    index=False
)

print("\nData successfully loaded into SQL Server!")


# ==========================================
# 5. VERIFY TABLE AND RECORD COUNT
# ==========================================

with engine.connect() as connection:

    result = connection.execute(
        text("""
            SELECT COUNT(*)
            FROM dbo.Netflix_Customers
        """)
    )

    total_records = result.scalar()

    print("\nTotal Records Loaded:")
    print(total_records)


# ==========================================
# 6. DISPLAY TABLE DATA FROM SQL SERVER
# ==========================================

with engine.connect() as connection:

    result = connection.execute(
        text("""
            SELECT TOP 5 *
            FROM dbo.Netflix_Customers
        """)
    )

    print("\nData Retrieved From SQL Server:")

    for row in result:
        print(row)


# ==========================================
# 7. CLOSE CONNECTION
# ==========================================

engine.dispose()

print("\nPipeline Completed Successfully!")
