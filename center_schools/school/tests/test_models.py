from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from school.models import Person
from school.serializers import PersonSerializer, PersonDetailSerializer


PERSONS_URL = reverse('school:person-list')
ME_URL = reverse('user:me')


def user_detail_url(user_id):
    """Return person detail URL"""
    return reverse('school:person-detail', args=[user_id])


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


class PublicPersonsApiTests(TestCase):
    """Test the publicly available persons API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving persons"""
        res = self.client.get(PERSONS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivatePersonsApiTests(TestCase):
    """Test the authorized user persons API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@mail.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_authenticated_user_personal_data_detail(self):
        """Test retrieving user personal data"""
        url = user_detail_url(self.user.id)
        res = self.client.get(url)

        serializer = PersonDetailSerializer(self.user.person)
        self.assertEqual(res.data, serializer.data)

    # # A list of persons only can be retrieved for a group admin user
    # def test_retrieve_persons(self):
    #     """Test retrieving persons"""
    #     sample_person(self.user)
    #     sample_person(self.user)
    #     res = self.client.get(PERSONS_URL)

    #     persons = Person.objects.all().order_by('-last_name')
    #     serializer = PersonSerializer(persons, many=True)
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertEqual(res.data, serializer.data)
