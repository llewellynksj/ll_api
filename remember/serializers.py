from django.db import IntegrityError
from rest_framework import serializers
from .models import Remember


class RememberSerializer(serializers.ModelSerializer):
    """
    Remember Serializer
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Remember
        fields = ['id', 'created_at', 'user', 'leaf']