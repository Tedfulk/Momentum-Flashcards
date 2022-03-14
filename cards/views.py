from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Deck, User, Card
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

    return render(request, "cards/add_card.html", {"form": form})


@login_required
def edit_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'GET':
        form = CardForm(instance=card)
    else:
        form = CardForm(data=request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect(to='card_list')

    return render(request, "cards/edit_card.html", {
        "form": form,
        "card": card
    })


@login_required
def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        card.delete()
        return redirect(to='card_list')
    return render(request, "cards/delete_card.html", {"card": card})


@login_required
def card_list(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    # cards = Card.objects.filter(deck_id=pk)
    cards = deck.cards.all()
    return render(request, "cards/card_list.html", {"cards": cards, "decks": deck})


# def login(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     return render(request, "cards/login.html")


# def home(request):
#     if request.user.is_authenticated:
#         return redirect("list_albums")
#     return render(request, "music/home.html")
