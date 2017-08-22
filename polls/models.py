import datetime
from django.db import models

# Create your models here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return  self.pub_date>=timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Person(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    area=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    def getPersonByArea(self):
        if self.area=="Dhanmondi":
            return self.name
