from rest_framework import serializers
from .models import Leaf


class LeafSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    account_id = serializers.ReadOnlyField(source='user.account.id')
    account_image = serializers.ReadOnlyField(source='user.account.image.url')
    remember_count = serializers.ReadOnlyField()

    def validate_image(self, value):
      if value.size > 1024 * 1024 * 2:
        raise serializers.ValidationError(
          'Image size should be less than 2MB'
        )
      if value.image.width > 4096:
        raise serializers.ValidationError(
          'Image width should be less than 4096px'
        )
      if value.image.height > 4096:
        raise serializers.ValidationError(
          'Image height should be less than 4096px'
        )
      return value

    def get_is_user(self, obj):
        request = self.context.get('request')
        return request.user == obj.user

    class Meta:
        model = Leaf
        fields = ['id', 'user', 'created_at', 'updated_at', 'name', 'memory', 'parent1', 'parent2', 'due_date', 'birth_date', 'weight', 'quotation', 'image', 'account_id', 'account_image', 'is_user', 'remember_count']