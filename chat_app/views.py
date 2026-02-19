from django.shortcuts import render
from .models import Chat
from django.http import JsonResponse
import json
# Create your views here.


def chat_view(request):
    if request.method == "GET":
        chats = list(Chat.objects.values())
        return JsonResponse(chats, safe=False)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)
            Chat.objects.create(
                name=data.get('name'),
                message=data.get('message')) 
        except:
            return JsonResponse("Das hat nicht geklappt mit dem Post.")
        


