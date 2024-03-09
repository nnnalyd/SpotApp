from django.shortcuts import render
from django.http import *
import getToken
import json

# Create your views here.
def displayAPI(request):
    token = getToken.get_token()
    response  = getToken.search_for_artist(token, "Frank Ocean")
    response_str = response['artists']
    return render(request, 'show.html', {'data' : response_str})