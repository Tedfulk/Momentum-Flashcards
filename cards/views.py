from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Deck, User
from .forms import CardForm, DeckForm


# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "cards/login.html")


@login_required
def home(request):  # this will include our list of the decks. Kind of like list_books or list_albums in other projects
    decks = Deck.objects.all()
    return render(request, "cards/home.html", {"decks": decks})


@login_required
def add_card(request):
    if request.method == 'GET':
        form = CardForm()
    else:
        form = CardForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='card_list')

    return render(request, "cadrs/add_card.html", {"form": form})

# def login(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     return render(request, "cards/login.html")


# def home(request):
#     if request.user.is_authenticated:
#         return redirect("list_albums")
#     return render(request, "music/home.html")
