from django.db import models

# Create your models here.


class create(models.Model):
    company_name = models.CharField(max_length=100)
    bug_name = models.CharField(max_lenght= 300)
    bug_detail = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.company_name