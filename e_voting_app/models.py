from django.contrib.auth.models import AbstractUser
from django.db import models


class Voter(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)

    def __str__(self):
        return f"""
        fullName:{self.first_name} {self.last_name}
        dob: {self.date_of_birth}
        """


class Poll(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE, unique=True)
    party = models.ForeignKey('Party', on_delete=models.PROTECT)


class Party(models.Model):
    acronym = models.CharField(max_length=255, blank=False, null=False, unique=True)
    full_name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    flag_bearer = models.ForeignKey(Voter, on_delete=models.PROTECT, unique=True)

    def __str__(self):
        return f"{self.acronym} {self.flag_bearer.first_name}"
