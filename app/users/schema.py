import graphene
from graphql_auth import mutations
from graphql_auth.schema import MeQuery, UserQuery


class AuthMutation(graphene.ObjectType):
    """
    This AuthMutation class consists of mutations for various functions such as create user and update user.
    It also has inheritances from django-graphql-inheritances
    """

    # Register a new user
    create_user = mutations.Register.Field()
    # Verify account using link sent to email
    verify_account = mutations.VerifyAccount.Field()
    # Resend link sent to email to verify account
    resend_activation_email = mutations.ResendActivationEmail.Field()
    # Login the user
    login_user = mutations.ObtainJSONWebToken.Field()

    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    # Update  a user's details
    update_user = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    """
    This class contains the fields of models that are supposed to be
    mutated.
    """

    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
