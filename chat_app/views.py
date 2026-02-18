from django.shortcuts import render
from .models import Chat
from django.http import JsonResponse
# Create your views here.


def chat_view(request):
    if request.method == "GET":
        chats = Chat.objects.all()
        
        chat_list = []
        for c in chats:
            chat_list.append({
                "name": c.name,
                "message": c.message,
                "created_at": str(c.created_at)
            })
        
        return JsonResponse({"results": chat_list})

    if request.method == "Post":
        print("Das hier ist POST")