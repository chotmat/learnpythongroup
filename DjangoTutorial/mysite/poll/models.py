from django.db import models

# Create your models here.
class Question(object):
    question_test = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
        
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)