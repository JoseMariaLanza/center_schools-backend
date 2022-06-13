from django.contrib.auth.models import Group
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from school.models import Person
from user.models.User import User

from school import serializers


class BasePersonAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """Base viewset for Person"""
    authentication_classes = (TokenAuthentication,)
    permisson_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only', 0))
        )
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(person__isnull=False)

        return queryset.filter(
            user=self.request.user
        ).order_by('-id').distinct()

    # def perform_create(self, serializer):
    #     """Create a new object"""
    #     serializer.save(user=self.request.user)


# class PersonViewSet(viewsets.ModelViewSet):
#     """Manage persons in the database"""
#     serializer_class = serializers.PersonSerializer
#     # members = User.objects.filter(groups__id__in=[User.groups.field])
#     # queryset = Person.objects.filter(user__in=members)
#     queryset = Person.objects.all()
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def _params_to_ints(self, qs):
#         """Convert a list of IDs to a list of integers"""
#         return [int(str_id) for str_id in qs.split(',')]

#     def get_queryset(self):
#         """Retrieve the graduations for the authenticated user"""
#         graduations = self.request.query_params.get('graduations')
#         groups = self.request.user.groups.all()
#         members = User.objects.filter(groups__id__in=groups)
#         queryset = self.queryset
#         if graduations:
#             graduation_ids = self._params_to_ints(graduations)
#             queryset = queryset.filter(graduations__id__in=graduation_ids)
#         if members:
#             queryset = queryset.filter(user__id__in=members)

#         return queryset

#     def get_serializer_class(self):
#         """Return appropiate serializer class"""
#         return self.serializer_class
#         # NO FUNCA
#         # return serializers.PersonDetailSerializer

#     # def perform_create(self, serializer):
#     #     """Create a new person"""
#     #     serializer.save(user=self.request.user)


class MembersViewSet(viewsets.ModelViewSet):
    """Retrieve users for school user admin authenticated"""
    serializer_class = serializers.UserProfileSerializer
    queryset = Person.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser,)

    def get_queryset(self):
        """Retrieve members of a school for the admin
            school user authenticated"""
        groups = Group.objects.filter(user=self.request.user)
        users = User.objects.filter(groups__id__in=groups)

        queryset = self.queryset
        queryset = queryset.filter(user__in=users)

        return queryset

    # def _params_to_ints(self, qs):
    #     """Convert a list of IDs to a list of integers"""
    #     return [int(str_id) for str_id in qs.split(',')]


class ManageUserProfileView(generics.RetrieveUpdateAPIView):
    """Manage authenticated user profile"""
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user profile"""
        return Person.objects.get(user=self.request.user)


# NO FUNCA
# members = PersonViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# profile = UserProfileViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })
