from django.db import models

# Create your models here.
class profile(models.Model):
    user = models.CharField(max_length=120)
    description = models.TextField(null=True)
    location = models.CharField(max_length=120, blank=True, null=True)
    job = models.CharField(max_length=120, blank=True, null=True)

    # Remember to use __str__ above. It is for Python 3.5 (our env). __unicode__ is for Python 2.7
    def __str__(self):
        return self.user

