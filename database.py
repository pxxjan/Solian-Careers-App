from sqlalchemy import create_engine, Table, MetaData

db_path = r'C:\Users\Lenovo\OneDrive\Desktop\Flask App\sqlite\solian.db'

engine = create_engine(f'sqlite:///{db_path}', echo=True)

metadata = MetaData()
metadata.reflect(bind=engine)

table_name = 'jobs'
table = metadata.tables[table_name]


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(table.select())

    column_names = result.keys()
    rows = result.fetchall()

    rows_as_dicts = [dict(zip(column_names, row)) for row in rows]

    return rows_as_dicts

def load_job_from_db(id):
    with engine.connect() as conn:
        query = table.select().where(table.c.id == id)
        result = conn.execute(query)
        row = result.fetchone()

    if row is not None:
        column_names = result.keys()
        job_dict = dict(zip(column_names, row))
        return job_dict
    else:
        return None
