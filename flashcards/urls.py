"""flashcards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cards import views as flash_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', flash_views.login, name='login'),
    path('cards/', flash_views.home, name='home'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('deck/adddeck/', flash_views.add_deck, name='add_deck'),
    path('deck/<int:deck_pk>/deletedeck/',
         flash_views.delete_deck, name='delete_deck'),
    path('deck/<int:deck_pk>/editdeck/',
         flash_views.edit_deck, name='edit_deck'),
    path('cards/<int:pk>/', flash_views.card_list, name='card_list'),
    path('deck/<int:deck_pk>/run', flash_views.run_deck, name='run_deck'),
    path('deck/<int:deck_pk>/results', flash_views.results, name='results'),
    path('deck/<int:deck_pk>/cards/<int:pk>/correct',
         flash_views.add_correct, name='correct'),
    path('cards/<int:pk>/incorrect', flash_views.incorrect, name='incorrect'),
    path('cards/<int:card_pk>/edit/', flash_views.edit_card, name='edit_card'),
    path('cards/<int:card_pk>/delete/',
         flash_views.delete_card, name='delete_card'),
    path('cards/<int:pk>/add/', flash_views.add_card, name='add_card'),
]
