import sqlalchemy

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://PythonMySQL:test123@localhost/python_test_1'

# Test if it works
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
print(engine.table_names())