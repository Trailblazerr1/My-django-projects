from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from .fbb1 import fbdata,activity,topfrnd,photo
from .models import Play
from .indi import *
import requests
import json


from allauth.socialaccount import providers
from allauth.socialaccount.models import SocialLogin, SocialToken, SocialApp
from allauth.socialaccount.providers.facebook.views import fb_complete_login
from allauth.socialaccount.helpers import complete_social_login
import allauth.account
from django.http import HttpResponse


def home(request):
    #user = request.user
   # user= request.user
   # access = SocialToken.objects.filter(account__user=user, account__provider='facebook')
    access_token = 'EAAZAtnvu9OZCUBAMEeRx6uZAIVazkX9IYNKgL32xoJWIfZCOOucGxeyrjelHBxsInmvamjx9o01s0SUewPZB5lTtDUTwkL32dU3Fl0aJ0tUZCWgCZAJHewl6enLF9tNwdDcs8cne5cEVm0bD9Cjk9H5VfrsiefIWNb8jXCNHKKokwZDZD'
   # access_token = str(access_token)
  #  r = requests.get('https://graph.facebook.com/me?access_token='+str(access_token)+'&fields=id,name,email') #MY_CORRECT_TOKEN&fields=id,name,email
  #  r = requests.get('https://graph.facebook.com/me?access_token='+access_token+'&fields=id,name,email') #add access_token.token to your request
   # r='hey there!'
    return access_token

def graph(request):
    tok = home(request)
    luv = lovejson0(tok)
    luv0 = luv[0]
    luv1 = luv[1]
    tt = []
    for i in luv1:
        tt.append(i['value'])
    ids = photo(tok,luv0)
    return render(request, 'app/abc.html', {'js0':  luv0 , 'js1':luv1 ,'tt':tt , 'ids':ids})

def play_count_by_month(request):
    tok = home(request)
    words = getwords(tok)
    return JsonResponse(words, safe=False)

#============================================================================
def timelinejson(request):
    tok = home(request)
    data = fbdata(tok)
    return JsonResponse(data, safe=False)

def timeline(request):
    return render(request, 'app/timeline.html')

#=============================================================================
def catchjson0(request):
    tok = home(request)
    data = activity(tok)
    return JsonResponse(data[0], safe=False)
def catchjson1(request):
    tok = home(request)
    data = activity(tok)
    return JsonResponse(data[1], safe=False)    
def catchjson2(request):
    tok = home(request)
    data = activity(tok)
    return JsonResponse(data[2], safe=False)
def catchjson3(request):
    tok = home(request)
    data = activity(tok)
    return JsonResponse(data[3], safe=False)

def catch(request):
    return render(request, 'app/pieperfect.html')

#=============================================================================

def lovejson0(request):
    tok = home(request)
    data = topfrnd(tok)
    return data

def lovejson1(request):
    tok = home(request)
    data = topfrnd(tok)
    return JsonResponse(data, safe=False)

def love(request):
    return render(request, 'app/love.html')