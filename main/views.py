from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests

def home(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())
@csrf_exempt
def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        token = getSpotifyAccessToken()
        list = requests.get(f"https://api.spotify.com/v1/search?q={query}&type=track&limit=5", headers={'Authorization': 'Bearer '+ token})
        print(list.json())
        return JsonResponse({'searchResults': list.json()})
    else:
        return JsonResponse({"message": "failed"})

def track(request, id):
    token = getSpotifyAccessToken()
    url = f"https://api.spotify.com/v1/tracks/{id}"
    headers = {'Authorization' : 'Bearer '+ token }
    response = requests.get(url, headers=headers)
    context = response.json()
    print(context['name'])
    template = loader.get_template('track.html')
    return HttpResponse(template.render({'context': context}, request))

def getSpotifyAccessToken():
        url = "https://accounts.spotify.com/api/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
                "grant_type": "client_credentials",
                "client_id": "08de4eaf71904d1b95254fab3015d711",
                "client_secret": "622b4fbad33947c59b95a6ae607de11d"
               }
        response = requests.post(url, headers=headers, data=data)
        token = response.json()['access_token']
        return token