import os
from sqlalchemy import  create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base

sqlite_file_name = '../../database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# crear motor de base de datos con la url
# el parametro echo se utiliza para mostrar en consola lo que genera la bd
engine = create_engine(database_url, echo=True)

# se requiere una session para poder manejar la bd
Session = sessionmaker(bind=engine)

#
Base = declarative_base()

