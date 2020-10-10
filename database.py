from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    last_known_location = Column(String)


class Contacts(Base):
    __tablename__ = 'contacts'
    contact_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    email = Column(String)


class Activities(Base):
    __tablename__ = 'activities'
    activity_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    contact_id = Column(Integer, ForeignKey('contacts.contact_id'))
    contact_method = Column(String)
    label = Column(String)
    tracking = Column(Boolean)
    start_datetime = Column(DateTime)
    end_datetime = Column(DateTime)
    contact_alerted = Column(Boolean)
    is_active = Column(Boolean)


class UserActivities(Base):
    __tablename__ = 'user_activities'
    user_activity_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    activity_id = Column(Integer, ForeignKey('activities.activity_id'))


class UserContacts(Base):
    __tablename__ = 'user_contacts'
    user_contact_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    contact_id = Column(Integer, ForeignKey('contacts.contact_id'))
