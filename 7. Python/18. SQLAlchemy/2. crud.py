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

# CRUD
def create_user(session, name, age):
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    return new_user

def get_users_list(session):
    users = session.query(User).all()
    return users

def get_user_by_id(session, user_id):
    # 1. old version
    # user = session.query(User).filter_by(id=user_id).first()
    # return user

    # 2. new version
    return session.get(User, user_id)

def update_user_age(session, user_id, new_age):
    user = session.get(User, user_id)

    if not user:
        return False
    
    user.age = new_age
    session.commit()

    return True

def delete_user_by_id(session, user_id):
    user = session.get(User, user_id)

    if not user:
        return False
    
    session.delete(user)
    session.commit()

    return True

def delete_user_by_name(session, name):
    # user = session.get(User, user.name)

    users = session.query(User).filter_by(name=name).all()

    if not users:
        return 0
    
    for u in users:
        session.delete(u)
        session.commit()

    return len(users) # 삭제된 col의 개수

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # 1. create user
        user1 = create_user(session, '김민정', 24)
        user2 = create_user(session, '김정민', 42)
        print(f'Users created: {user1.id}, {user2.id}')

        # 2. find users
        user = get_user_by_id(session, user1.id)
        print(f'Info of this user: {user.name}, {user.age}')

        users = get_users_list(session)
        print(f'All of users')
        for u in users:
            print(f' - {u.id}: {u.name}, {u.age}')

        # 3. update user info
        updated_user = update_user_age(session, user2.id, 40)
        print(f'Info of this user: {get_user_by_id(session, user2.id).name}, {get_user_by_id(session, user2.id).age}')
        
        # 4. delete user
        deleted_user_count = delete_user_by_name(session, '고길동')
        print(f'{deleted_user_count} columns are deleted')

        users = get_users_list(session)
        print(f'All of users')
        for u in users:
            print(f' - {u.id}: {u.name}, {u.age}')