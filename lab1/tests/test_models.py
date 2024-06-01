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

    def test_user_first_name(self):
        self.assertEqual(self.user.first_name, "John")

    def test_user_last_name(self):
        self.assertEqual(self.user.last_name, "Doe")

    def test_user_phone_number(self):
        self.assertEqual(self.user.phone_number, "754262432")

    def test_user_residence(self):
        self.assertEqual(self.user.residence, "Nairobi")

    def test_user_email(self):
        self.assertEqual(self.user.email, "doejohn22@example.com")

    def test_user_age(self):
        self.assertEqual(self.user.age, 36)

    def test_user_is_active(self):
        self.assertEqual(self.user.is_active, True)

    def test_user_dob(self):
        self.assertEqual(self.user.dob, "1994-04-13")

    def test_user_created_at(self):
        # Using almostEqual to account for slight differences in time
        self.assertAlmostEqual(
            self.user.created_at, timezone.now(), delta=timezone.timedelta(seconds=1)
        )

    def test_user_updated_at(self):
        self.assertAlmostEqual(
            self.user.updated_at, timezone.now(), delta=timezone.timedelta(seconds=1)
        )

    def test_user_str(self):
        self.assertEqual(
            str(self.user),
            f"{self.user.first_name} has successfully created. Users's id: {self.user.user_id}",
        )
