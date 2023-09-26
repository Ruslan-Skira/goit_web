from rel_one_to_many import User, Article, session

user = User(name='Boris Johnson')
session.add(user)
session.commit()

article = Article(title='Our country’s saddest day', content='Lorem ipsum...', user_id=user.id)
session.add(article)
session.commit()