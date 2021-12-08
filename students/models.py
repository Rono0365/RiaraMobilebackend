from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from noticeboard import serializers
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    #created = models.DateTimeField(auto_now_add=True)
    School = models.CharField(max_length=100, blank=True, default='')
    id_no = models.CharField(max_length=100, blank=True, default='')
    Course =  models.CharField(max_length=100, blank=True, default='')
    valid_till = models.CharField(max_length=100, blank=True, default='')
    class Meta:
        ordering = ['first_name']
class Unit(models.Model):#this is like a subject example physics or philosophy
    unit_name = models.CharField(max_length=100, blank=True, default='')#Computer organisation
    School = models.CharField(max_length=100, blank=True, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    duration =  models.CharField(max_length=100, blank=True, default='')
    Topic = models.CharField(max_length=100, blank=True, default='')
    day_taught = models.CharField(max_length=100, blank=True, default='')
    time_taught = models.CharField(max_length=100, blank=True, default='')
    assignment =  models.CharField(max_length=100, blank=True, default='')#if any then activate the submitted or not submitted in accordance to days submitted
    valid_till = models.CharField(max_length=100, blank=True, default='')
    assignment_till = models.CharField(max_length=100,default='')#this must be activated on assignment given
    class Meta:
        #unique_together = ['day_taught','unit_name']
        ordering = ['unit_name']

class Course(models.Model):
    units = models.CharField(max_length=100, blank=True, default='')#no_of_units offered in the school institution.i.e:oop,co, etc...
    #last_name = models.CharField(max_length=100, blank=True, default='')
    #created = models.DateTimeField(auto_now_add=True)
    valid_till = models.CharField(max_length=100, blank=True, default='')
    

    class Meta:
        ordering = ['units']
