from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///alchemy-example.db')

# Define a object
Base = declarative_base()

# Defina a table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)

# Execute
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name = '홍길동', age = 25)
session.add(new_user)

new_user = User(name = '고길동', age = 32)
session.add(new_user)

session.commit()

users = session.query(User).all()
for user in users:
    print(user.name, user.age)