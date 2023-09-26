from rel_one_to_many import User, Article, session

user = User(name='Boris Johnson2')
session.add(user)
session.commit()

article = Article(title='Our country’s saddest day', content='Lorem ipsum...', user_id=user.id)
session.add(article)
session.commit()

article = Article(title='fresh title', content='anythin ', user_id=user.id)
session.add(article)
session.commit()