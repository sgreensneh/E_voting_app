from rest_framework import serializers

from e_voting_app.models import Voter, Poll, Party


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ['first_name', 'last_name', 'date_of_birth']


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['voter', 'party']


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['acronym', 'full_name', 'flag_bearer']
