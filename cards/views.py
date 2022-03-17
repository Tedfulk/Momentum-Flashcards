from ast import If
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Deck, User, Card
from .forms import CardForm, DeckForm, CardUpdateForm


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


@login_required
def add_card(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'GET':
        form = CardForm()
    else:
        form = CardForm(data=request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.deck = deck
            card.save()
            return redirect(to='card_list', pk=deck.pk)

    return render(request, "cards/add_card.html", {"form": form, "deck": deck})


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
    return render(request, "cards/card_list.html", {"deck": deck})


def run_deck(request, deck_pk):
    # need to get deck
    deck = get_object_or_404(Deck, pk=deck_pk)
    # check to see if any of the cards are true
    # if no cards are false then reset all deck cards to false
    # if Card.objects.filter(deck_id=deck, card_seen=False).exists():
    #     # TODO change redirect to a results page
    #     return redirect(to='home')
    card = Card.objects.all().filter(deck_id=deck, card_seen=False).first()
    deck_length = Card.objects.all().filter(deck_id=deck).count()

    return render(request, "cards/run_deck.html", {"deck": deck, "card": card, "deck_length": deck_length})


def add_correct(request, deck_pk, pk):
    # breakpoint()
    deck = get_object_or_404(Deck, pk=deck_pk)
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        card_form = CardUpdateForm(data=request.POST, instance=card)
        if card_form.is_valid():
            card_form = card_form.save(commit=False)
            card_form.card_seen = True
            card_form.save()
            deck.correct_count += 1
            deck.save()
        return redirect('run_deck', deck_pk=deck_pk)


def incorrect(request, deck_pk, pk):
    deck = get_object_or_404(Deck, deck_pk=pk)
    card = get_object_or_404(Card, card_pk=pk)
    if request.method == 'GET':
        correct = Card
    else:
        correct = Card(request.method == 'POST')
        Card.objects.filter(pk=deck_pk).update(card_seen=True)
        return redirect(to="run_deck", deck_pk=deck_pk)

    return render(request, "cards/correct.html", {"deck": deck, "card": card, "correct": correct})


def results(request, deck_pk):
    pass
