from database import Users, Contacts, Activities, UserActivities, UserContacts, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///Files/data.sqlite')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


class DatabaseHandler:
    def __init__(self):
        self.engine = create_engine('sqlite:///Files/data.sqlite')
        self.session = sessionmaker(bind=self.engine)()

    def query(self, sql_statement):
        return [x for x in self.engine.execute(sql_statement)]

    def commit(self, sql_statement):
        try:
            self.engine.execute(sql_statement)
            self.session.commit()
            return True
        except Exception:
            return False

    def _create_database(self):
        Base.metadata.create_all(bind=self.engine)

    def _wipe_tables(self):
        tables = ['users', 'activities', 'contacts', 'user_activities', 'user_contacts']
        [self.commit(f"DELETE FROM {table}") for table in tables]

    def __exit__(self):
        self.session.close()


if __name__ == '__main__':
    db_handler = DatabaseHandler()
    # db_handler._create_database()
