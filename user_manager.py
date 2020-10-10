from database_handler import DatabaseHandler, Users


class UserManager(DatabaseHandler):
    def __init__(self):
        super().__init__()

    def create_user(self, first, last, email):
        user = Users()
        user.first_name = first
        user.last_name = last
        user.email = email
        self.session.add(user)
        self.session.commit()


if __name__ == '__main__':
    manager = UserManager()
    manager.create_user("Coty", "Fivecoat", "Fiveoat@gmail.com")
