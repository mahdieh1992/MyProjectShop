from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation as PasswordValidate

user=get_user_model()

class RegisterUserSerializer(serializers.Serializer):
    Email=serializers.EmailField()
    Password=serializers.CharField()
    Confirm_Password=serializers.CharField()


    def validate(self, data):
        email=data.get('Email')
        password=data.get('Password')
        confirm_password=data.get('Confirm_Password')
        
        if password!=confirm_password:
            raise ValidationError('password and confirm_password is not match',code='not_match_password')
        if user.objects.filter(email=email).exists:
            raise ValidationError('user is already exists',code='exists-email')
        
        try:
            PasswordValidate.validate_password(password=password)
        except ValidationError as err:
            raise ValidationError({'detail':tuple(err.message)})
        
    def create(self, validated_data):
       validated_data.pop('confirm_password')
       data=[field for field in validated_data]
       print(data)
       return user.objects.create(**data) 

        

