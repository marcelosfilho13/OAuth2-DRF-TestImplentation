from rest_framework.views import APIView
from rest_framework.response import Response


#! Import OAuth2 permission classes
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class ExampleAPIView(APIView):
    #! Protecting the endpoint with OAuth2 scopes (scope: read)
    permission_classes = [TokenHasScope]
    required_scopes = ['read']

    def get(self, request):
      #! the information to be returned by the API after token validation
        data = {
            "message": "Hello, this is a protected API endpoint!"
        } 