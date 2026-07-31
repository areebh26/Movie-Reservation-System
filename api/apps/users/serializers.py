from rest_framework import serializers

from apps.users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        trim_whitespace=False,
    )
    
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "name",
            "gender",
            "date_joined"
        ]
        read_only_fields = ["id","date_joined"]
        
        

   

    def create(self, validated_data):
        return User.objects.create_user(
        email=validated_data["email"],
        password=validated_data["password"],
        name=validated_data["name"],
        gender=validated_data.get("gender"),
    )



class UserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "email",
            "password"
        ]




class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "gender",
            "date_joined",
            "phone",
        ]
        read_only_fields = ["id","date_joined"]



class ProfilePicUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "profile_pic",
        ]
        
            
        