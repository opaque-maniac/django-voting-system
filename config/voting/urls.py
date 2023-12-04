from django.urls import path

from . import views

app_name = 'voting'

urlpatterns = [
    path('', views.index, name='index'),
    path('election/<int:election_id>/', views.election, name='election'),
    path('candidate/<int:candidate_id>/', views.individual_candidate, name='individual_candidate'),
    path('party/<int:party_id>/', views.individual_party, name='individual_party'),
    path('election/all/', views.all_elections, name='all_elections'),
    path('election/new/', views.new_election, name='new_election'),
    path('candidate/all/', views.all_candidates, name='all_candidates'),
    path('candidate/new/', views.new_candidate, name='new_candidate'),
    path('party/all/', views.all_parties, name='all_parties'),
    path('party/new/', views.new_party, name='new_party'),
    path('election/<int:election_id>/vote/', views.vote, name='vote'),
    path('election/<int:election_id>/results/', views.results, name='results'),
]
