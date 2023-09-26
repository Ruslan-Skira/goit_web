from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, String, Integer, Text, ForeignKey

engine = create_engine("sqlite:///CRUD_07_01.db")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base() #As introduced at Declarative Mapping, the Declarative style includes the ability to generate a mapped Table object at the same time, or to accommodate a Table or other FromClause object directly.


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    articles = relationship('Article', back_populates='author')


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer(), primary_key=True)
    title = Column(String(255))
    content = Column(Text())
    user_id = Column(Integer(), ForeignKey('users.id'))
    author = relationship('User', back_populates='articles')


Base.metadata.create_all(engine)
Base.metadata.bind = engine