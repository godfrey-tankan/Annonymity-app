from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Confession


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ["user", "bio"]


class ConfessionSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Confession
        fields = ["id", "author", "topic", "content", "created_at"]
