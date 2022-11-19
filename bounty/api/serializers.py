
from django.db.models import fields
from rest_framework import serializers
from .models import Item
  
class create(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('company_name', 'bug_name', 'bug_detail')