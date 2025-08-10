from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('user_name', 'user_email', 'password')
    
    def create(self, validated_data):
        user = User.objects.create_user(
            user_email=validated_data['user_email'],
            user_name=validated_data['user_name'],
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        user_email = data.get('user_email')
        password = data.get('password')
        
        if user_email and password:
            user = authenticate(user_email=user_email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid credentials')
            if not user.is_active:
                raise serializers.ValidationError('User account is disabled')
            data['user'] = user
        else:
            raise serializers.ValidationError('Must include email and password')
        
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_name', 'user_email', 'created_on', 'last_update')
        read_only_fields = ('user_id', 'created_on', 'last_update')
