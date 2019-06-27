
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):

    username = serializers.HiddenField(default = 'user')
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)

    class Meta:

        model = get_user_model()
        exclude = ('username', 'password2',)

    def save(self, request):

        data = request.data

        User = get_user_model()

        first_name = data.get('first_name')
        last_name = data.get('last_name')

        username = first_name + ' ' + last_name


        email = data.get('email')
        password1 = data.get('password1')

        UserInstance = User(username = username, email = email, first_name = first_name, last_name = last_name, password = password1)
        
        UserInstance.save()

        return UserInstance

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = '__all__'