from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import time

from .models import Election
from .models import Party
from .models import Candidate
from .models import Vote

from .forms import NewElectionForm
from .forms import NewCandidateForm
from .forms import NewPartyForm
from .forms import NewVoteForm

# Create your views here.
def index(request):
    elections = Election.objects.all()
    context = {'elections': elections}
    return render(request, 'voting/index.html', context)

@login_required
def election(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    parties = Party.objects.filter(election=election_id)
    canditates = Candidate.objects.filter(election=election_id)
    context = {'election': election, 'parties': parties, 'candidates': canditates}
    return render(request, 'voting/election.html', context)

@login_required
def individual_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    context = {'candidate': candidate}
    return render(request, 'voting/individual_candidate.html', context)

@login_required
def individual_party(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    context = {'party': party}
    return render(request, 'voting/individual_party.html', context)

@login_required
def all_elections(request):
    elections = Election.objects.all()
    context = {'elections': elections}
    return render(request, 'voting/all_elections.html', context)

@login_required
def new_election(request):
    if request.method == 'POST':
        form = NewElectionForm(request.POST)
        if form.is_valid():
            election = form.save(commit=False)
            election.created_by = request.user
            election.save()
            return redirect('voting:index')
    else:
        form = NewElectionForm()
        context = {'form': form}
        return render(request, 'voting/new_election.html', context)
    
@login_required
def all_candidates(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'voting/all_candidates.html', context)

@login_required
def new_candidate(request):
    if request.method == 'POST':
        form = NewCandidateForm(request.POST)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.save()
            return redirect('voting:index')
    else:
        form = NewCandidateForm()
        context = {'form': form}
        return render(request, 'voting/new_candidate.html', context)

@login_required
def all_parties(request):
    parties = Party.objects.all()
    context = {'parties': parties}
    return render(request, 'voting/all_parties.html', context)

@login_required
def new_party(request):
    if request.method == 'POST':
        form = NewPartyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voting:index')
    else:
        form = NewPartyForm()
        context = {'form': form}
        return render(request, 'voting/new_party.html', context)
    
@login_required
def vote(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    if election.end_date.timestamp < time.time():
        return redirect('voting:election', args=[int(election_id)])
    parties = Party.objects.filter(election=election_id)
    canditates = Candidate.objects.filter(election=election_id)
    
    if request.method == 'POST':
        form = NewVoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.election = election
            vote.voter = request.user
            vote.save()
            return redirect('voting:index')
    else:
        form = NewVoteForm()
    context = {'election': election, 'parties': parties, 'candidates': canditates}
    return render(request, 'voting/vote.html', context)

@login_required
def election_votes(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    votes = Vote.objects.filter(election=election_id)
    candidates = Candidate.objects.filter(election=election_id)
    context = {'election': election, 'votes': votes}
    return render(request, 'voting/election_votes.html', context)