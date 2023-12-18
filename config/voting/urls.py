from django.urls import path
from . import views

app_name = "voting"

# Urls for the voting application
urlpatterns = [
    path('', views.index, name='index'),
    path('elections/new/', views.new_election, name='new_election'),
    path('elections/<int:election_id>/', views.individual_election, name='individual_election'),
    path('candidates/new/', views.new_candidate, name='new_candidate'),
    path('candidates/<int:candidate_id>/', views.individual_candidate, name='individual_candidate'),
    path('party/new/', views.new_party, name='new_party'),
    path('party/<int:party_id>/', views.individual_party, name='individual_party'),
    path('vote/<int:candidate_id>/', views.vote, name='vote'),
    path('search/', views.search, name='search'),
]