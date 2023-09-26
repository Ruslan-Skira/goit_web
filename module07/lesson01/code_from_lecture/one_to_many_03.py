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

users= session.query(User).filter_by(name='Peter Miller').all()

for user in users:
    for article in user.articles:
        print(article.title, user.name)

#-----
article = session.query(Article).filter_by(title='Our country’s saddest day').one()

print(article.title, article.author.name)

# ---------Many to many

class User(Base):
    """Here used backref as back_populates but need only in one class"""
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    userinfo = relationship('UserInfo', backref='user', uselist=False)  # uselist arguments for  many to one relationship


class UserInfo(Base):
    __tablename__ = 'userinfo'
    id = Column(Integer(), primary_key=True)
    telegram = Column(String(11))
    phone = Column(String(11))
    site = Column(String(64))
    user_id = Column(Integer(), ForeignKey('users.id'))