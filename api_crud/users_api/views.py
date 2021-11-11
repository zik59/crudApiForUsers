from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users_api.serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """"API endpoint that allows users to be viewed or edited"""
    queryset = User.objects.all()
    serializer_class = ReadOnlyUserSerializer
    
    def create(self, request):
        serializer = WriteOnlyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_read_serializer = ReadOnlyUserSerializer()
            return Response(user_read_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):  
        serializer = WriteOnlyUserSerializer(data=request.data)              
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(pk=pk)
            user_read_serializer = ReadOnlyUserSerializer(user)
            return Response(user_read_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):    
        serializer = WriteOnlyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(pk=pk)
            user_read_serializer = ReadOnlyUserSerializer(user)
            return Response(user_read_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    