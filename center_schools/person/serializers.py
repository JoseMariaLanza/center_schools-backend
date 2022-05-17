from rest_framework import serializers
from person.models import Person, Graduation


class PersonSerializer(serializers.ModelSerializer):
    """Serializer for person objects"""

    class Meta:
        model = Person
        fields = (
            'id',
            'user_id',
            'first_name',
            'last_name',
            'birth_date',
            'blood_type',
            'observation',
            'status',
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
        )
        read_only_fields = ('id',)


class PersonDetailSerializer(PersonSerializer):
    """Serializer for a user personal data"""
    # graduations = GraduationSerializer(many=True, read_only=True)
