import graphene
from graphql_auth import mutations
from graphql_auth.schema import MeQuery, UserQuery


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
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
