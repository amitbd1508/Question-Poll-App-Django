terminal command

-for start a project
django-admin startproject mysite

-for crate a app
python3 manage.py  startapp polls

-for run the server
python3 manage.py runserver


-after creating app must declure urls.py
urlpatterns =[
    url(r'$',views.index,name='index')
]

-for save database change
python3 manage.py migrate

-for seeing sql query
python3 manage.py sqlmigrate polls 0001


-for make change in app models
python manage.py makemigrations polls

-django shell
python manage.py shell

##########################################################


#django shell


from polls.models import Question, Choice

from django.utils import timezone
Question.objects.all()
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()

Question.objects.get(pub_date__year=current_year)
q = Question.objects.get(pk=1)
q.was_published_recently()
q.choice_set.count()
q.choice_set.all()