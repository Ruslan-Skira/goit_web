from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

"Database	/Users/ruslanskira/PycharmProjects/goit/python-web-practice/alembci_learn/alembci_learn.db"
engine = create_engine("sqlite:///../alembci_learn.db")
Session = sessionmaker(bind=engine)
session = Session()