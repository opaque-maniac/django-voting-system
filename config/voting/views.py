from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils import timezone
from django.db.models import F, Count

from accounts.models import Profile
from . import models

# View for the homepage
def index(request):
    elections = models.Election.objects.filter()[:5]
    context = { 'elections': elections }
    return render(request, 'voting/index.html', context)

# View for the individual elections page
@login_required
def individual_election(request, election_id):
    election = models.Election.objects.get(id=election_id)
    vote = models.Vote.objects.filter(user=request.user, election=election).exists()
    candidates = models.Candidate.objects.filter(election=election_id)
    has_voted = vote
    
    if election.end_date >= timezone.now():
        context = {
            'election': election,
            'candidates': candidates,
            'has_voted': has_voted,
            'has_ended': False,
        }
    else:
        results = []
        for candidate in candidates:
            votes_for_candidate = models.Vote.objects.filter(candidate=candidate).count()
            results.append({ 'candidate': candidate, 'votes': votes_for_candidate })
        results = sorted(results, key=lambda x: x['votes'], reverse=True)
        context = {
            'election': election,
            'has_voted': has_voted,
            'has_ended': True,
            'results': results,
        }
    return render(request, 'voting/individual_election.html', context)

# View for the individual candidate page
@login_required
def individual_candidate(request, candidate_id):
    candidate = models.Candidate.objects.get(id=candidate_id)
    context = { 'candidate': candidate }
    return render(request, 'voting/individual_candidate.html', context)

# View for the individual party page
@login_required
def individual_party(request, party_id):
    party = models.Party.objects.get(id=party_id)
    context = { 'party': party }
    return render(request, 'voting/individual_party.html', context)

# View for the individual voting page
@login_required
def vote(request, candidate_id):
    has_voted = models.Vote.objects.filter(user=request.user).exists()
    if has_voted:
        raise Http404
    else:
        candidate = models.Candidate.objects.filter(id=candidate_id)
        election = candidate.election
        vote = models.Vote.objects.create(candidate=candidate, election=election, user=request.user)
        vote.save()
        candidate.vote_count = F('vote_count') + 1
        candidate.save()
        election.vote_count = F('vote_count') + 1
        election.save()
        return redirect('voting:individual_election', args=(election.id,))
