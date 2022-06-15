from rest_framework import generics, viewsets, authentication
from rest_framework.permissions import IsAuthenticated, \
    BasePermission
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer
from school.models.Person import Person
from school.serializers import PersonSerializer, UserAccountSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user


class IsAdminUser(BasePermission):
    """Allow access only to superusers"""

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class SystemUsersViewSet(viewsets.ModelViewSet):
    """Retrieve all system users for superuser"""
    serializer_class = UserAccountSerializer
    queryset = Person.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser,)


class ManagePersonalDataView(generics.RetrieveUpdateAPIView):
    """Manage authenticated user profile"""
    serializer_class = PersonSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_object(self):
        """Retrieve and return authenticated user profile"""
        return Person.objects.get(user=self.request.user)


class ManageAccountView(generics.RetrieveUpdateAPIView):
    """Manage authenticated user account"""
    serializer_class = UserAccountSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user profile"""
        return Person.objects.get(user=self.request.user)
