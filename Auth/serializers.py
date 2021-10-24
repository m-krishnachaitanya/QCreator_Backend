from rest_framework import serializers
from Auth.models import *

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('username',
                  'password',
                  'email',
                  'name')