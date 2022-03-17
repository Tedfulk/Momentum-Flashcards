from django import forms
from .models import Deck, Card, User


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = [
            'title',
            'description',
        ]


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            'word',
            'definition',
        ]


class CardUpdateForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            'card_seen',
        ]
