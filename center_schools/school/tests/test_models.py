from django.test import TestCase
from school.models import Person  # , Graduation
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test School models"""

    def sample_user(self, email='test@mail.com', password='testpass'):
        """Create a sample user"""
        return get_user_model().objects.create_user(email, password)

    def test_create_user_profile_data_at_create_user(self):
        """Test creating a new person at create a new user is successful"""
        self.sample_user()
        # user = self.sample_user()
        # user_profile_data = Person.objects.get(id=user.id)

        # self.assertEqual(user_profile_data.user.id, user.id)
        self.assertTrue(Person.objects.all().exists())
