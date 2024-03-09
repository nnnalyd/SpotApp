from django.shortcuts import render
from django.http import *
import getToken
import json

# Create your views here.
def displayAPI(request):
    token = getToken.get_token()
    response  = getToken.getArtist(token)
    response_str = response["name"]
    return render(request, 'show.html', {'data' : response_str})