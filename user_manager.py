from database_handler import DatabaseHandler, Users
from random import choice


class UserManager(DatabaseHandler):
    def __init__(self):
        super().__init__()

    def insert(self, user):
        self.session.add(user)
        self.session.commit()

    def create_user(self, first, last, email):
        user = Users()
        user.first_name = first
        user.last_name = last
        user.email = email
        self.session.add(user)
        self.session.commit()


if __name__ == '__main__':
    manager = UserManager()
    last_names = ["Smith", "Johnson", "Hansen", "Brown", "Jones", "Miller", "Davis"]
    first_names = ["James", "Mary", "John", "Robert", "William", "David", "Daniel", "Charles", "Paul"]
    created = 0
    while created < 50:
        first = choice(first_names)
        last = choice(last_names)
        manager.create_user(first, last, f"{first.lower()}.{last.lower()}@gmail.com")
        created += 1
