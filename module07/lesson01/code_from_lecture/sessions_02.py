from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sql_module02_l01.db')
DBSession = sessionmaker(bind=engine)  # Lazy object run when you need
session = DBSession()

Base = declarative_base()  # connects an sync tables and


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship(Person)

Base.metadata.create_all(engine)  # create tables in DB
Base.metadata.bind = engine

# insert data into db
new_person = Person(name="Bill")
session.add(new_person)
print(new_person.id)
session.commit()  # write data to db

new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
# save to db
session.commit()

# Query form db
for person in session.query(Person).all():  # get data from db
    print(person.name)

for adr in session.query(Address).all():
    print(adr.post_code, 'ADRESS')