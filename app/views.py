from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import re

# Create your views here.
class validate(APIView):
    def post(self,request):
        print(request.data)
        if re.search("https://www.google.com/search?", request.data['url']):
            return Response("Invalid url")
        return Response("Valid url")