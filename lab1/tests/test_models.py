from django.test import TestCase
from django.utils import timezone

from orm.models import User


class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            phone_number="754262432",
            residence="Nairobi",
            email="doejohn22@example.com",
            age=36,
            is_active=True,
            dob="1994-04-13",
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )

    def test_user_creation(self):
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.phone_number, "754262432")
        self.assertEqual(self.user.residence, "Nairobi")
        self.assertEqual(self.user.email, "doejohn22@example.com")
        self.assertEqual(self.user.age, 36)
        self.assertEqual(self.user.is_active, True)
        self.assertEqual(self.user.dob, "1994-04-13")
        self.assertEqual(self.user.created_at, timezone.now())
        self.assertEqual(self.user.updated_at, timezone.now())

    def test_user_str(self):
        self.assertEqual(
            str(self.user),
            f"{self.user.first_name} has successfully created. Users's id: {self.user.user_id}",
        )
