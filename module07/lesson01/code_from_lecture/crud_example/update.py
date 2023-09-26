from rel_one_to_many import User, Article, session

article = session.query(Article).get(1)
article.content = 'Very important content for the article'
session.add(article)
session.commit()