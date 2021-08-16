from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free.

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    use_in_migrations = True

    def create_user(self, **kwargs):
        """
        Create and return a `User` with the given email, username and password.
        """

        username = kwargs.get("username")
        email = kwargs.get("email")
        password = kwargs.get("password")
        if not username:
            raise ValueError("Username is required.")

        if not email:
            raise ValueError("Email address is required.")

        if not kwargs.get("password"):
            raise ValueError("Password is required.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.save()

        return user

    def create_superuser(self, **kwargs):
        """
        Create and return a `User` with superuser powers.

        Superuser powers means that this user is an admin that can do anything
        they want.
        """
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractUser):
    """
    User class implementing a fully featured User Model.

    The AbstractUser class has username and password as required fields
    and all other fields as optional.
    We override the email field to make it required, and unique for our app.
    """

    email = models.EmailField(db_index=True, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.email

    def get_short_name(self) -> str:
        """
        Return the short name for the user as username
        """
        return self.username
