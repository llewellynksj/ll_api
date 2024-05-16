from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context.get('request')
        return request.user == obj.user

    class Meta:
        model = Account
        fields = ['id', 'user', 'created_at', 'updated_at', 'name', 'image', 'is_user']
