from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
User = get_user_model()

class UserCreateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','name','phone','address','college','password')

    def validate(self,data):
        user = User(**data)
        password = data.get('password')

        try:
            validate_password(password,user)
        except exceptions.ValidationError as e:
            serializers_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {'password':serializers_errors['non_field_errors']}
            )
        
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            phone = validated_data['phone'],
            address =  validated_data['address'],
            college = validated_data['college'],
            password = validated_data['password'],
        )

        return user
            
class UserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','name','phone','address','college')
        