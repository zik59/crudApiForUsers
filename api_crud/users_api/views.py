from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.models import User
from users_api.serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def users_list(request):
    """Get full list of users or create a new user with post """
    if request.method == 'GET':
        return getAllUsers()

    elif request.method == 'POST':
        return createUser(request)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def crud_for_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return getUserById(user)

    elif request.method == 'PUT':
        return putUpdateUserById(request, user)

    elif request.method == 'PATCH':
        return patchUpdateUserById()

    elif request.method == 'DELETE':
        return deleteUserById(user)

def getAllUsers():
    """"Returns the list of information about all users"""
    users = User.objects.all()
    users_serializer = ReadOnlyUserSerializer(users, many=True)
    return JsonResponse(users_serializer.data, safe=False)

def createUser(request):
    """Creates new user and returns data of this user"""
    user_data = JSONParser().parse(request)
    user_serializer = WriteOnlyUserSerializer(data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getUserById(user):
    """"returns user's data by id"""
    user_serializer = ReadOnlyUserSerializer(user)
    return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)

def putUpdateUserById(request, user):
    """"Updates user's data by id and creates new one with this data"""
    user_data = JSONParser().parse(request)
    user_serializer = WriteOnlyUserSerializer(user, data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        user_read_serializer = ReadOnlyUserSerializer(user)
        return JsonResponse(user_read_serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def patchUpdateUserById(request, user):
    user_data = JSONParser().parse(request)
    user_serializer = WriteOnlyUserSerializer(user, data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        user_read_serializer = ReadOnlyUserSerializer(user)
        return JsonResponse(user_read_serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteUserById(user):
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)