from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Deck, User




# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "cards/login.html")

@login_required
def home(request):   #this will include our list of the decks. Kind of like list_books or list_albums in other projects
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