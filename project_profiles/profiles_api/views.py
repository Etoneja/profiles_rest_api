from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions


class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiview = [
            "feature 1",
            "feature 2",
            "feature 3",
        ]

        return Response({
            "message": "Hello!",
            "an_apiview": an_apiview
        })

    def post(self, request):

        serializer = serializers.HelloSerializer(
            data=request.data
        )

        if serializer.is_valid():
            name = serializer.data.get("name")

            message = f"Hello {name}"

            return Response({
                "message": message
            })
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):

        return Response({
            "method": "put"
        })

    def patch(self, request, pk=None):

        return Response({
            "method": "patch"
        })

    def delete(self, request, pk=None):

        return Response({
            "method": "delete"
        })


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):

        a_viewset = [
            "bla 1",
            "bla 2",
            "bla 3"
        ]

        return Response({
            "message": "Hello",
            "a_viewset": a_viewset
        })

    def create(self, request):

        serializer = serializers.HelloSerializer(
            data=request.data
        )
        if serializer.is_valid():
            name = serializer.data.get("name")
            message = f"Hello {name}"
            return Response({
                "message": message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):

        return Response({
            "method": "get"
        })

    def update(self, request, pk=None):

        return Response({
            "method": "put"
        })

    def partial_update(self, request, pk=None):

        return Response({
            "method": "patch"
        })

    def destroy(self, request, pk=None):

        return Response({
            "method": "delete"
        })


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ("name", "email")


class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self, request):

        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ProfileFeedSerializer
    authentication_classes = (TokenAuthentication, )
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.PostOwnStatus, IsAuthenticated
    )

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
