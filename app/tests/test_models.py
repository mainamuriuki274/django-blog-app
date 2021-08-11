# tests for app models
import pytest

from ..models import User


@pytest.mark.django_db
class TestUserModel:
    """
    This class defines the tests for the user model.
    """

    def test_raises_error_when_no_username_is_supplied(self):
        """
        Test the user model raises an error when no username is supplied.
        """
        user_data = {
            "email": "testemail@test.com",
            "password": "testPassword123",
        }
        user = User(user_data)
        with pytest.raises(ValueError):
            user.save()

    def test_raises_error_when_no_email_is_supplied(self):
        """
        Test the user model raises an error when no email is supplied.
        """
        user_data = {
            "username": "testUsername",
            "password": "testPassword123",
        }
        user = User(user_data)
        with pytest.raises(ValueError):
            user.save()

    def test_raises_error_when_no_password_is_supplied(self):
        """
        Test the user model raises an error when no email is supplied.
        """
        user_data = {
            "username": "testUsername",
            "email": "testemail@test.com",
        }
        user = User(user_data)
        with pytest.raises(ValueError):
            user.save()

    def test_model_can_create_user(self):
        """
        Test the user model can create a new user.
        """
        user_data = {
            "username": "testUsername",
            "email": "testemail@test.com",
            "password": "testPassword123",
        }
        user = User(user_data)
        user.save()
        assert User.objects.count() == 1

    def test_raises_error_when_existing_email_is_supplied(self):
        """
        Test the user model raises an error when an existing email is supplied.
        """
        user_data = {
            "username": "testUsername2",
            "email": "testemail@test.com",
            "password": "testPassword123",
        }
        user = User(user_data)
        with pytest.raises(ValueError):
            user.save()

    def test_raises_error_when_existing_username_is_supplied(self):
        """
        Test the user model raises an error when an existing email is supplied.
        """
        user_data = {
            "username": "testUsername",
            "email": "testemail2@test.com",
            "password": "testPassword123",
        }
        user = User(user_data)
        with pytest.raises(ValueError):
            user.save()
