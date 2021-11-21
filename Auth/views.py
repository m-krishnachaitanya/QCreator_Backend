from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from Auth.serializers import *
from Auth.models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello World!!")

@api_view(['POST'])
def register(request):
    login_data = JSONParser().parse(request)
    login_serializer = LoginSerializer(data=login_data)
    if login_serializer.is_valid():
        login_serializer.save()
        return HttpResponse(login_serializer.data, status=status.HTTP_201_CREATED)
    return HttpResponse(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def verify(request):
    login_data = JSONParser().parse(request)
    username = login_data.get('username')
    password = login_data.get('password')
    user = Login.objects.all().filter(username = username, password = password)
    if len(user) == 0:
        return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return HttpResponse(status=status.HTTP_200_OK)