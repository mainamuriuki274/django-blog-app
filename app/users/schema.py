import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

User = get_user_model()


class UserType(DjangoObjectType):
    """Class that contains the important fields of user table and model"""

    class Meta:
        model = User
        fields = "__all__"


class UserInput(graphene.InputObjectType):
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()


class CreateUser(graphene.Mutation):
    """
    This is the main class where user object is created.
    This class must implement a mutate method.
    """

    class Arguments:
        """
        class argument allows us to define a paramenter
        to save data to the database
        """

        input = UserInput(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, input):
        user = User(username=input.username, email=input.email)
        user.set_password(input.password)

        user.save()
        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    """
    This is the main class where user object is updated.
    This class must implement a mutate method.
    """

    class Arguments:
        """
        class argument allows us to define paramenters
        to update a user's details in the database
        """

        id = graphene.ID()
        input = UserInput(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, input, id):
        user = User.objects.get(id=id)
        user.username = input.username
        user.email = input.email
        user.password = input.password
        user.save()

        return UpdateUser(user=user)


class DeleteUser(graphene.Mutation):
    """
    This is the main class where user object is deleted.
    This class must implement a mutate method.
    """

    class Arguments:
        """
        class argument allows us to define a paramenter 'id'
        to delete a user from the database
        """

        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id):
        user = User.objects.get(id=id)
        user.delete()

        return


class Mutation(graphene.ObjectType):
    """
    This class contains the fields of models that are supposed to be
    mutated.
    Defines mutations and sends params such as updating and creating data
    to the model
    """

    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_users(root, info, **kwargs):
        # Querying a list
        return User.objects.all()

    def resolve_user(root, info, **kwargs):
        # Querying a specific user
        return User.objects.get(id=kwargs.get("id"))


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
    # adding mutations to our schema
)
