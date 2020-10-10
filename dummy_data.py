from database_handler import DatabaseHandler, Users, Activities, Contacts
from random import choice
from datetime import datetime


class DummyManager(DatabaseHandler):
    def __init__(self):
        super().__init__()

    def create_user(self, first, last, email):
        user = Users()
        user.first_name = first
        user.last_name = last
        user.email = email
        self.insert(user)

    def create_contact(self, first, last, phone_number, email):
        contact = Contacts()
        contact.first_name = first
        contact.last_name = last
        contact.phone_number = phone_number
        contact.email = email
        self.insert(contact)

    def create_activity(self, contact_method, label):
        activity = Activities()
        activity.contact_method = contact_method
        activity.contact_id = 1
        activity.tracking = True
        activity.start_datetime = datetime.now()
        activity.end_datetime = datetime.utcnow()
        activity.contact_alerted = False
        activity.is_active = True
        activity.label = label
        self.insert(activity)


if __name__ == '__main__':
    manager = DummyManager()
    last_names = ["Smith", "Johnson", "Hansen", "Brown", "Jones", "Miller", "Davis"]
    first_names = ["James", "Mary", "John", "Robert", "William", "David", "Daniel", "Charles", "Paul"]
    contact_methods = ["email", "text", "messenger"]
    labels = ["Hike", "Date", "Lunch", "Backcounty Skiing", "Rock Climbing", "In Laws"]
    numbers = ["801.445.3903", "801.232.2344", "801.234.3985", "208.484.4840"]
    created = 0
    while created < 50:
        first = choice(first_names)
        last = choice(last_names)
        manager.create_user(first, last, f"{first.lower()}.{last.lower()}@gmail.com")
        first = choice(first_names)
        last = choice(last_names)
        manager.create_contact(first, last, choice(numbers), f"{first.lower()}.{last.lower()}@gmail.com")
        manager.create_activity(choice(contact_methods), choice(labels))
        created += 1
