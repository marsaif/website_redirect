from django.db import models


# Create your models here.
class UrlRedirect(models.Model):
    job_id = models.CharField(max_length=1000,default='')
    url = models.CharField(max_length=1000,default='')
    clicks = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
