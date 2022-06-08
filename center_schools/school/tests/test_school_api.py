from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from school.models import Person
from school.serializers import UserProfileSerializer


# Routes for superusers
# api/1.1/school/members
PERSONS_URL = reverse('school:person-list')

# Route for logged in user


def user_profile_url():
    """Return person detail URL"""
    return reverse('school:profile')


def sample_user():
    """Create a commen user"""
    user = get_user_model().objects.create_user(
        'commonuser@mail.com',
        'testpass'
    )
    return user


def sample_superuser():
    """Create a commen user"""
    user = get_user_model().objects.create_superuser(
        'superuser@mail.com',
        'testpass'
    )
    return user


def sample_person(user, **params):
    """Create and return a sample person"""
    defaults = {
        'first_name': 'Test Person first name',
        'last_name': 'last name',
        'birth_date': '1988-08-07',
        'blood_type': 'A',
        'observation': 'Its healty',
        'status': 'Student'
    }
    defaults.update(params)

    return Person.objects.create(user=user, **defaults)


class PublicSchoolApiTests(TestCase):
    """Test the publicly available persons API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving user personal data"""
        url = user_profile_url()
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_school_members(self):
        """Test that login is required for retrieving a
        list of school members"""
        res = self.client.get(PERSONS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    """Here goes tests that login and instructor or editor? (editor=staff)
    role is required to show users member of a school"""


class PrivateSchoolApiTests(TestCase):
    """Test the authorized user persons API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_authenticated_user_profile_success(self):
        """Test retrieving user personal data"""
        user = sample_user()
        self.client.force_authenticate(user)

        url = user_profile_url()
        res = self.client.get(url)

        user_data = Person.objects.get(user=user)
        serializer = UserProfileSerializer(user_data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_update_authenticated_user_profile(self):
        """Thest that updating profile data"""
        pass

    # region Admin Users only
    def test_retrieve_school_members_forbidden_to_user(self):
        """Test that a common user is not authorized to view school members"""
        user = sample_user()
        self.client.force_authenticate(user)

        res = self.client.get(PERSONS_URL)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_school_members_to_superuser(self):
        """Test that a superuser can view all users"""
        user = sample_superuser()
        self.client.force_authenticate(user)

        res = self.client.get(PERSONS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
    # endregion

    # region Staff Only
    # REFACTOR |
    # retrieve user list if is staff and person.status is instructor?
        """Create a new view that retrieve a list of users
        if authenticated user is staff and is instructor once tests are crated
        """
    # endregion
