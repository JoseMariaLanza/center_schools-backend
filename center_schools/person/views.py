from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from person.models import Person

from person import serializers


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

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class PersonViewSet(viewsets.ModelViewSet):
    """Manage persons in the database"""
    serializer_class = serializers.PersonSerializer
    queryset = Person.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the graduations for the authenticated user"""
        graduations = self.request.query_params.get('graduations')
        queryset = self.queryset
        if graduations:
            graduation_ids = self._params_to_ints(graduations)
            queryset = queryset.filter(graduation__id__in=graduation_ids)

        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """Return appropiate serializer class"""
        # return self.serializer_class
        return serializers.PersonDetailSerializer

    def perform_create(self, serializer):
        """Create a new person"""
        serializer.save(user=self.request.user)
