from sqlalchemy import create_engine, MetaData

# Define the path to your SQLite database
db_path = r'C:\Users\Lenovo\OneDrive\Desktop\Flask App\sqlite\solian.db'

# Create an engine to connect to the database
engine = create_engine(f'sqlite:///{db_path}', echo=True)

# Initialize a new Metadata object
metadata = MetaData()

# Reflect tables from the database
metadata.reflect(bind=engine)

# Print out the list of table names reflected from the database
print("Tables reflected from the database:")
for table_name in metadata.tables.keys():
    print(table_name)
