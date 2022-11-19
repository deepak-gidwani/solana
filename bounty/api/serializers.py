from django.db.models import fields
from rest_framework import serializers
from .models import BugBounty

class BugBountySerializer():
    class Meta:
        model = BugBounty
        fields = "__all__"