from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from time import time

from . import models
from . import forms

# View for the index page
def index(request):
    elections = models.Election.objects.all()
    context = {'elections': elections}
    return render(request, 'polling/index.html', context)

# View for individual election
@login_required
def individual_election(request, election_id):
    election = get_object_or_404(models.Election, pk=election_id)
    candidates = models.Candidate.objects.filter(election=election)
    parties = models.Party.objects.filter(election=election)
    context = {
        'election': election,
        'candidates': candidates,
        'parties': parties,    
    }
    return render(request, 'polling/individual_election.html', context)

# View for new election
@login_required
def new_election(request):
    if request.user.is_staff == False:
        raise Http404
    if request.method == 'POST':
        form = forms.ElectionForm(request.POST)
        if form.is_valid():
            election = form.save(commit=False)
            election.created_by = request.user
            election.save()
            return redirect('polling:index')
        else:
            context = {'errors': form.errors, 'form': form}
            return render(request, 'polling/new_election.html', context)
    else:
        context = {'form': forms.ElectionForm()}
        return render(request, 'polling/new_election.html', context)

# View for new candidate
@login_required
def new_candidate(request, election_id):
    if request.user.is_staff == False:
        raise Http404
    if request.method == 'POST':
        form = forms.CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save()
            return redirect('polling:individual_candidate', args=[int(candidate.id)])
        else:
            context = {'errors': form.errors, 'form': form}
            return render(request, 'polling/new_candidate.html', context)
    else:
        context = {'form': forms.CandidateForm()}
        return render(request, 'polling/new_candidate.html', context)
    
# View for individual candidate
@login_required
def individual_candidate(request, candidate_id):
    candidate = get_object_or_404(models.Candidate, pk=candidate_id)
    party = get_object_or_404(models.Party, pk=candidate.party.id)
    context = {'candidate': candidate, 'party': party}
    return render(request, 'polling/individual_candidate.html', context)

# View for new party
@login_required
def new_party(request):
    if request.user.is_staff == False:
        raise Http404
    if request.method == 'POST':
        form = forms.PatyForm(request.POST, request.FILES)
        if form.is_valid():
            party = form.save()
            return redirect('polling:individual_party', args=[int(party.id)])
        else:
            context = {'errors': form.errors, 'form': form}
            return render(request, 'polling/new_party.html', context)
    else:
        context = {'form': forms.PatyForm()}
        return render(request, 'polling/new_party.html', context)
    
# View for individual party
@login_required
def individual_party(request, party_id):
    party = get_object_or_404(models.Party, pk=party_id)
    candidates = models.Candidate.objects.filter(party=party)
    context = {'party': party, 'candidates': candidates}
    return render(request, 'polling/individual_party.html', context)

# View for voting
@login_required
def voting(request, election_id):
    election = get_object_or_404(models.Election, pk=election_id)
    if request.method == 'POST':
        form = forms.VotingForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.voter = request.user
            vote.election = election
            vote.save()
            return redirect('polling:individual_election', args=[int(election_id)])
        else:
            context = {'errors': form.errors, 'form': form}
            return render(request, 'polling/vote.html', context)
    else:
        context = {'election': election, 'form': forms.VotingForm()}
        return render(request, 'polling/vote.html', context)
    
# View for the results of an election
def results(request, election_id):
    election = get_object_or_404(models.Election, pk=election_id)
    if election.end_date.timestamp < time():
        raise Http404
    votes = models.Vote.objects.filter(election=election)
    candidates = models.Candidate.objects.filter(election=election)
    candidate_id = request.GET.get('candidate', 0)

    if candidate_id:
        votes = models.Vote.objects.filter(chosen_candidate=candidate_id)

    context = {
        'election': election,
        'votes': votes,
        'candidates': candidates,
    }
    return render(request, 'polling/results.html', context)

