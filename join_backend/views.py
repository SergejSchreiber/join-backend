from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets
from django.core import serializers
from join_backend.models import Todo
from join_backend.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [] # permissions.IsAuthenticated

    def create(self, request):
        todo = Todo.objects.create(
            title = request.data.get('title', ''),
            description = request.data.get('description', ''),
            user = request.user,
            )
        serialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serialized_obj, content_type='application/json')