from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from e_voting_app.models import Voter, Poll, Party
from e_voting_app.serializer import VoterSerializer, PollSerializer, PartySerializer


class VoterViewSet(ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer


class PollViewSet(ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PartyViewSet(ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
