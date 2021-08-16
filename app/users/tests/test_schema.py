import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase
from graphene.test import Client
from mixer.backend.django import mixer

from app.users.schema import schema

User = get_user_model()


@pytest.mark.django_db
class TestUserSchema(TestCase):
    def setUp(self):
        self.client = Client(schema)

    def test_query_users(self):
        query_payload = """
            query{
                users {
                    edges {
                        node{
                            username
                            email
                        }
                    }
                }
            }
        """
        response = self.client.execute(query_payload)
        users = response.get("data").get("users").get("edges")
        assert len(users) == 0

        mixer.blend(User)
        response = self.client.execute(query_payload)
        users = response.get("data").get("users").get("edges")
        assert len(users) == 1
