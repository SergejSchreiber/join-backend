from django.contrib.auth.models import Group, User
from rest_framework import serializers
from join_backend.models import Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'created_at', 'user', 'time_passed']