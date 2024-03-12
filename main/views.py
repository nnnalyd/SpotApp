from django.shortcuts import render
from django.http import *
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import*
from . models import *
import getToken
import json

# Create your views here.

#displaying the api requests
def displayAPI(request):
    token = getToken.get_token()
    response  = getToken.getArtist(token)
    response_str = response["name"]
    response_img= response["images"][2]["url"]
    return render(request, 'show.html', {'image' : response_img, 'data' : response_str})

class ReactView(APIView):
    def get(self, request):
        output = [{"user": output.user, "userType": output.userType}
                   for output in React.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)