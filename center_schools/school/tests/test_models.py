from django.test import TestCase
from school.models import Person  # , Graduation
from django.contrib.auth import get_user_model


def sample_user(email='test@mail.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test School models"""

    def setUp(self):
        self.user = sample_user()

    def test_create_user_profile_data_at_create_user_success(self):
        """Test creating a new person at create a new user is successful"""

        exists = Person.objects.filter(user=self.user).exists()
        self.assertTrue(exists)
