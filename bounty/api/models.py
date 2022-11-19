from django.db import models

# Create your models here.
class BugBounty():
    company_name = models.CharField(max_length=100)
    bug_name = models.CharField(max_length=100)
    bug_detail = models.TextField()
