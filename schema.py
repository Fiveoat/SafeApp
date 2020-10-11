import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from database_handler import db_session, Users as UsersModel, Activities as ActivitiesModel, Contacts as ContactsModel, \
    UserActivities as UserActivitiesModel, UserContacts as UserContactsModel


class Users(SQLAlchemyObjectType):
    class Meta:
        model = UsersModel
        interfaces = (relay.Node,)


class Activities(SQLAlchemyObjectType):
    class Meta:
        model = ActivitiesModel
        interfaces = (relay.Node,)


class Contacts(SQLAlchemyObjectType):
    class Meta:
        model = ContactsModel
        interfaces = (relay.Node,)


class UserActivities(SQLAlchemyObjectType):
    class Meta:
        model = UserActivitiesModel
        interfaces = (relay.Node,)


class UserContacts(SQLAlchemyObjectType):
    class Meta:
        model = UserContactsModel
        interfaces = (relay.Node,)


# NOT SURE HOW THESE WORK
class CreateUser(graphene.Mutation):
    class Input:
        user_id = graphene.Int()
        first_name = graphene.String()
        email = graphene.String()
        last_name = graphene.String()
        last_known_location = graphene.String()
    ok = graphene.Boolean()
    user = graphene.Field(Users)

    @staticmethod
    def mutate(___, args, _, __):
        user = UsersModel()
        user.first_name = args.get("first_name")
        user.last_name = args.get("last_name")
        user.email = args.get("email")
        user.last_known_location = args.get("last_known_location")
        db_session.add(user)
        db_session.commit()
        ok = True
        return CreateUser(user=user, ok=ok)


class CreateActivity(graphene.Mutation):
    class Input:
        contact_id = graphene.String()
        label = graphene.String()
        tracking = graphene.Boolean()
        contact_alerted = graphene.Boolean()
        is_active = graphene.Boolean()
    ok = graphene.Boolean()
    activity = graphene.Field(Activities)

    @staticmethod
    def mutate(___, args, _, __):
        activity = ActivitiesModel()
        activity.contact_id = args.get("contact_id")
        activity.label = args.get("label")
        activity.tracking = args.get("tracking", False)
        activity.start_datetime = args.get("start_datetime")
        activity.end_datetime = args.get("end_datetime")
        activity.contact_alerted = args.get("contact_alerted", False)
        activity.is_active = args.get("is_active", True)
        db_session.add(activity)
        db_session.commit()
        ok = True
        return CreateActivity(activity=activity, ok=ok)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(Users)
    all_activities = SQLAlchemyConnectionField(Activities)
    all_contacts = SQLAlchemyConnectionField(Contacts)
    # NOT SURE HOW THESE WORK
    find_user = graphene.Field(lambda: Users, user_id=graphene.Int())
    find_contacts = graphene.Field(lambda: Contacts, contact_id=graphene.Int())
    find_activity = graphene.Field(lambda: Activities, activity_id=graphene.Int())

    # NOT SURE HOW THESE WORK
    @staticmethod
    def resolve_find_user(args, context):
        query = Users.get_query(context)
        user_id = args.get('user_id')
        # you can also use and_ with filter() eg: filter(and_(param1, param2)).first()
        return query.filter(UsersModel.user_id == user_id).first()

    @staticmethod
    def resolve_find_contact(args, context):
        print(args)
        print(context)
        query = Contacts.get_query(context)
        contact_id = args.get('contact_id')
        return query.filter(ContactsModel.contact_id == contact_id).first()


class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_activity = CreateActivity.Field()


schema = graphene.Schema(query=Query, types=[Users, Activities, Contacts, UserContacts, UserActivities],
                         mutation=MyMutations)
