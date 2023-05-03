from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id', 'username', 'email',
            'last_name', 'first_name'
        ]
