from django.shortcuts import render, redirect, get_object_or_404
from .models import Deck



# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "cards/login.html")

def home(request):
    decks = Deck.objects.all()
    return render(request, "cards/home.html", {"decks": decks})

# def login(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     return render(request, "cards/login.html")



# def home(request):
#     if request.user.is_authenticated:
#         return redirect("list_albums")
#     return render(request, "music/home.html")