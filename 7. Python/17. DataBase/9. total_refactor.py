import database.my_crud_lib as db

def main():
    db.create_table()

    db.insert_user('Alice', 30)
    db.insert_user('Bob', 25)
    db.insert_user('Charlie', 35)

    print('Find User #1')
    users = db.get_users()
    for user in users:
        print(user)

    db.update_user('Alice', 40)
    db.update_user('Bob', 33)

    print('Find User #2')
    user = db.get_users_by_name('Alice')
    print(user)

    db.delete_user_by_name('Alice')
    users = db.get_users()

    print('Find User #3')
    users = db.get_users()
    print(users)

if __name__ == '__main__':
    main()