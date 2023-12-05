from django.urls import path

from . import views

app_name = 'polling'

urlpatterns = [
    path('', views.index, name='index'),
    path('elections/new/', views.new_election, name='new_election'),
    path('elections/<int:election_id>/', views.individual_election, name='individual_election'),
    path('candidates/new/', views.new_candidate, name='new_candidate'),
    path('candidates/<int:candidate_id>/', views.individual_candidate, name='individual_candidate'),
    path('parties/new/', views.new_party, name='new_party'),
    path('parties/<int:party_id>/', views.individual_party, name='individual_party'),
    path('elections/<int:election_id>/vote/', views.voting, name='voting'),
    path('elections/<int:election_id>/results/', views.results, name='results'),
]
