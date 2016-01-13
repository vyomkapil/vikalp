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
    branch = models.ForeignKey(Branch)
    name = models.CharField(max_length=20)
    about = models.TextField()
    proc = models.TextField('recruitment procedure')

    class Meta:
        verbose_name_plural = "companies"

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    contact_no = models.CharField(max_length=10)

    def __unicode__(self):
        return self.user.username



