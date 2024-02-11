from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):
    """test api views"""

    def get(self, request, format=None):
        """return list of api features"""
        an_api_view = ['User http methods as function( get, post, patch)',
                       'is similar to Django views',
                       'gives more control over application logic',
                       ]
        return Response({'message': 'hello', 'an_api_view': an_api_view})

