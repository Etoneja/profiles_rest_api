from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = [
            "id", "email", "name", "password"
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):

        user = models.UserProfile(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"]
        )
        user.set_password(user.password)
        user.save()
        return user


class ProfileFeedSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user_profile.name')

    class Meta:

        model = models.ProfileFeedItem
        fields = (
            "id", "user_profile",
            "status_text", "created_on", "username"
        )
        read_only_fields = ["user_profile"]
