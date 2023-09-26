from rel_one_to_many import User, Article, session

article = session.query(Article).get(1)
session.delete(article)
session.commit()