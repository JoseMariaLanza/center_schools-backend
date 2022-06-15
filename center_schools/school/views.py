from django.contrib.auth.models import Group
from rest_framework import viewsets, mixins
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


class MembersViewSet(viewsets.ModelViewSet):
    """Retrieve users for school user admin authenticated"""
    serializer_class = serializers.UserAccountSerializer
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


# class ManagePersonalDataView(generics.RetrieveUpdateAPIView):
#     """Manage authenticated user profile"""
#     serializer_class = serializers.PersonSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def get_object(self):
#         """Retrieve and return authenticated user profile"""
#         return Person.objects.get(user=self.request.user)
