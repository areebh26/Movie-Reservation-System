from rest_framework import serializers

from apps.users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "name",
            "gender"
        ]

    def validate_password(self,value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value



class UserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "email",
            "password"
        ]
            
        