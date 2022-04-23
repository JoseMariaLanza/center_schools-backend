from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful():
        """Test creating a new user with an email is successfus"""
        email = "test@mail.com"
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user_check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@MAIL.COM"
        user = get_user_model().objects.create_user(email, '123456')

        self.assertEqual(user.email, emali.lower())
