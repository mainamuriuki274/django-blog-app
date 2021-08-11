# tests for app views
from django.urls import reverse
import pytest

from ..models import User


@pytest.mark.django_db
class TestUserViews:
    """
    This class defines the tests for the user views.
    """

    def test_app_can_post_user(self, client):
        """
        Test app can create a user.
        """
        user_data = {
            "username": "testUsername",
            "email": "testemail@test.com",
            "password": "testPassword123",
        }
        assert User.objects.count() == 0
        response = client.post(reverse("user_list"), user_data)
        assert response.status_code == 201
        assert User.objects.count() == 1

    def test_app_can_get_a_user(self, client):
        """
        Test app can get a given user.
        """
        users = User.objects.count()
        assert users == 1
        response = client.get(reverse("user_detail", kwargs={"pk": 1}))
        assert response.status_code == 200

    def test_app_can_update_user(self, client):
        """
        Test app can update a given user.
        """
        user_data = {
            "username": "testUpdatedUsername",
            "email": "testUpdatedEmail@test.com",
            "password": "testUpdatedPassword123",
        }
        response = client.put(
            reverse("user_detail", kwargs={"pk": 1}), user_data
        )
        assert response.status_code == 200

    def test_app_can_delete_user(client, user_data):
        """
        Test app can delete a user.
        """
        response = client.delete(reverse("user_detail", kwargs={"pk": 1}))
        assert response.status_code == 204
