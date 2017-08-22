from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice, Person

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Person)
