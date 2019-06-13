from django.db import models


class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=42, unique=True)
    first_block = models.IntegerField(null=True)
    # updated = models.DateTimeField(auto_now=True)
