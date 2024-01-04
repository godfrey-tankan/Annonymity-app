from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Confession
from .serializers import ProfileSerializer, ConfessionSerializer


def index(request):
    return render(request, "index.html")


@api_view(["GET"])
def get_profiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)


@api_view(["POST"])
def create_confession(request):
    serializer = ConfessionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
