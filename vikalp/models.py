from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "branches"

    def __unicode__(self):
        return self.name

class Company(models.Model):
    user = models.ForeignKey(User, default=None)
    branch = models.ForeignKey(Branch)
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20, default=None)
    about = models.TextField()
    proc = models.TextField('recruitment procedure')
    location = models.CharField(max_length=10)
    ctc = models.CharField(max_length=5, default=0)
    experience = models.CharField(max_length=5, default=0)

    class Meta:
        verbose_name_plural = "companies"

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    contact_no = models.CharField(max_length=10)

    def __unicode__(self):
        return self.user.username



