from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item


engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

user1 = User(name="adeeb",
             email="adeebtwait@gmail.com",
             picture="https://via.placeholder.com/300/09f/fff.png")
session.add(user1)
session.commit()

category1 = Category(title="Basketball", user=user1)
session.add(category1)
session.commit()

category2 = Category(title="Soccer", user=user1)
session.add(category2)
session.commit()

category3 = Category(title="Snowboarding", user=user1)
session.add(category3)
session.commit()

category4 = Category(title="Football", user=user1)
session.add(category4)
session.commit()

item1 = Item(title="Goggles", description="lorem ipsum",
             category=category3, user=user1)
session.add(item1)
session.commit()


print "added menu items!"
