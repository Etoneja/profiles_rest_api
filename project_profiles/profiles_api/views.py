from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

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
