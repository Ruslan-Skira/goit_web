from rel_one_to_many import User, Article, session

articles = session.query(Article).all()
for article in articles:
    article.id = article.id + 1
    session.add(article)
    session.commit()