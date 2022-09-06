from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Importing Rest Framework tests tools
from rest_framework.test import APIClient
# APIClient is a test client to make requests to our API
# and check what the response is
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
USER_LIST_URL = reverse('user:list')
ME_URL = reverse('user:me')
USER_ACCOUNT = reverse('user:my-account')


def user_account_url(id):
    """Return person detail URL"""
    return reverse('user:account', args=[id])


def sample_common_user(**params):
    defaults = {
        'email': 'common_user@mail.com',
        'password': 'testpass',
        'username': 'Common user'
    }
    defaults.update(params)

    return get_user_model().objects.create_user(**defaults)


def sample_superuser(**params):
    """Create a superuser"""
    defaults = {
        'email': 'superuser@mail.com',
        'password': 'testpass'
    }
    defaults.update(params)

    return get_user_model().objects.create_superuser(**defaults)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    # setUp method is a constructor
    def setUp(self):
        self.user = sample_common_user()
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email': 'new_user@mail.com',
            'password': 'testpass',
            'username': 'Test Name'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(**res.data)

        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating user that already exists fail"""
        payload = {'email': 'common_user@mail.com', 'password': 'testpass'}

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 8 characters"""
        payload = {'email': 'new_user@mail.com', 'password': 'pass'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        # Each test refresh the DB so the user email created in the previous
        # tests are not going to be accessible en the current test
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {
            'email': 'new_user@mail.com',
            'password': 'testpass',
            'username': 'Common user'
        }
        sample_common_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid credentials are given"""
        payload = {
            'email': 'common_user@mail.com',
            'password': 'wrongpassword'
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesn't exists"""
        payload = {
            'email': 'unexistent_user@mail.com',
            'password': 'testpass'
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        res = self.client.post(TOKEN_URL, {'email': 'one', 'password': ''})

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieved_user_unauthorized(self):
        """Test that authentication is required for users"""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_user_list_to_unauthorized_user_fails(self):
        """Test that deny query to user list for unauthorized user"""
        self.client.force_authenticate(self.user)

        res = self.client.get(USER_LIST_URL)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class PrivateUserApiTests(TestCase):
    """Test API requests that require authentication"""

    # setUp occurs automatically before each test
    def setUp(self):
        self.user = sample_common_user(
            email='test@mail.com',
            password='testpass',
            username='Common user'
        )
        self.superuser = sample_superuser(
            email='superuser@mail.com',
            password='testpass'
        )
        self.client = APIClient()
        # self.client.force_authenticate(user=self.user)

    def test_retrieve_user_data_success(self):
        """Test retrieving user data for logged in user"""
        self.client.force_authenticate(user=self.user)
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'username': self.user.username,
            'email': self.user.email
        })

    def test_post_me_not_allowed(self):
        """Test that POST is not allowed on the me url"""
        self.client.force_authenticate(user=self.user)
        res = self.client.post(ME_URL, {})

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_data_success(self):
        """Test updating the user data for authenticated user is success"""
        payload = {'username': 'new username', 'password': 'newpassword'}

        self.client.force_authenticate(user=self.user)
        res = self.client.patch(ME_URL, payload)

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, payload['username'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_user_list_for_authenticated_superuser(self):
        """Test that retrieve system users list for superuser"""
        self.client.force_authenticate(self.superuser)
        res = self.client.get(USER_LIST_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_logged_in_user_account_success(self):
        """Test that retrieve user account by id"""
        self.client.force_authenticate(self.superuser)
        res = self.client.get(USER_ACCOUNT)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_user_account_by_id_success(self):
        """Test that retrieve user account by id"""
        self.client.force_authenticate(self.superuser)
        res1 = self.client.get(user_account_url(self.user.id))

        user2 = sample_common_user(
            email='sample@user.com',
            password='testpass',
            username='User Name'
        )
        res2 = self.client.get(user_account_url(user2.id))

        self.assertEqual(res2.status_code, status.HTTP_200_OK)
        # self.assertEqual(res2.data, {
        #     'email': user2.email,
        #     'username': user2.username
        # })
        self.assertEqual(res1.status_code, status.HTTP_200_OK)
        # self.assertEqual(res1.data, {
        #     'email': self.user.email,
        #     'username': self.user.username
        # })
