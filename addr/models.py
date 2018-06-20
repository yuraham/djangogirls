from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    memo = models.CharField(max_length=200, null=True, blank=True)
    home = models.CharField(max_length=200, null=True, blank=True)
    pone = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name