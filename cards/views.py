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
def add_deck(request):
    if request.method == 'POST':
        form = DeckForm(data=request.POST)
        if form.is_valid():
            deck = form.save()

            return redirect("home")
    else:
        form = DeckForm()

        return render(request, "cards/add_deck.html", {'form': form})


@login_required
def delete_deck(request, deck_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    if request.method == 'POST':
        deck.delete()
        return redirect(to='home')
    return render(request, "cards/delete_deck.html", {"deck": deck})


@login_required
def edit_deck(request, deck_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    if request.method == 'GET':
        form = DeckForm(instance=deck)
    else:
        form = DeckForm(data=request.POST, instance=deck)
        if form.is_valid():
            form.save()
            return redirect(to='home')

    return render(request, "cards/edit_deck.html", {
        "form": form,
        "deck": deck
    })

# add_card view isn't working. needs fixed


@login_required
def add_card(request):
    if request.method == 'GET':
        form = CardForm()
    else:
        form = CardForm(data=request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect(to='card_list')

    return render(request, "cards/add_card.html", {"form": form})


@login_required
def edit_card(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    if request.method == 'GET':
        form = CardForm(instance=card)
    else:
        form = CardForm(data=request.POST, instance=card)
        if form.is_valid():
            deck_pk = card.deck.pk
            form.save()
            return redirect(to='card_list', pk=deck_pk)

    return render(request, "cards/edit_card.html", {
        "form": form,
        "card": card
    })


@login_required
def delete_card(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    if request.method == 'POST':
        deck_pk = card.deck.pk
        card.delete()
        return redirect(to='card_list', pk=deck_pk)
    return render(request, "cards/delete_card.html", {"card": card, })


@login_required
def card_list(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    # cards = Card.objects.filter(deck_id=pk)
    cards = deck.cards.all()
    return render(request, "cards/card_list.html", {"cards": cards, "decks": deck})

def run_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    cards = deck.cards.all()
    return render(request, "cards/run_deck.html", {"cards": cards, "deck": deck})
    
   

# def login(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     return render(request, "cards/login.html")


# def home(request):
#     if request.user.is_authenticated:
#         return redirect("list_albums")
#     return render(request, "music/home.html")
