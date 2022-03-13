from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Deck(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Card(models.Model):
    word = models.CharField(max_length=500)
    definition = models.CharField(max_length=500)
    deck = models.ForeignKey(
        Deck, related_name="cards", on_delete=models.CASCADE
    )
    
# TODO make seperate pull request and change related name to "cards" so we can later do deck.cards

    def __str__(self):
        return self.word
