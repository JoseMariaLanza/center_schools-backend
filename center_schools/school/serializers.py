from rest_framework import serializers
from school.models import Person, Graduation
from user.serializers import UserSerializer


class PersonSerializer(serializers.ModelSerializer):
    """Serializer for person objects"""

    class Meta:
        model = Person
        fields = (
            'id',
            'user',
            'first_name',
            'last_name',
            'birth_date',
            'blood_type',
            'observation',
            'status'
        )
        read_only_fields = ('id',)


class GraduationSerializer(serializers.ModelSerializer):
    """Serializer for graduation objects"""

    class Meta:
        model = Graduation
        fields = (
            'id',
            'person_id',
            'graduation_date',
            'certification_id',
            'evaluator',
            'graduation_place',
            'graduations'
        )
        read_only_fields = ('id',)


class PersonDetailSerializer(PersonSerializer):
    """Serializer for person graduations"""
    graduations = GraduationSerializer(many=True, read_only=True)


class UserProfileSerializer(PersonSerializer):
    """Serializer for User personal data"""
    user = UserSerializer(read_only=True)
