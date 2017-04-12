from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from closuretree.models import ClosureModel

# Create your models here.
class Community(ClosureModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200,null=True ,blank=True)
    members_number = models.IntegerField(null=True ,blank=True)
    parent = models.ForeignKey('self', related_name='children',null=True,blank=True)
    # user = models.ManyToManyField(User)

    class Meta:
        db_table = 'community'


    def __unicode__(self):
        return '%s: %s' % (self.id, self.name)

    def __str__(self):
        return self.name


class User(AbstractUser):
    community = models.ForeignKey(Community,null=True ,blank=True)
    follow_communities = models.ManyToManyField(Community,related_name='+')

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'
