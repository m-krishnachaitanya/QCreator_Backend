from django.db import models

# Create your models here.
class Quizes(models.Model):
    quizid = models.CharField(primary_key = True, max_length = 10)
    userid = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Questions(models.Model):
    questionid = models.AutoField(primary_key = True, default = None)
    quizid = models.CharField(max_length = 10)
    question = models.CharField(max_length = 2048)
    option1 = models.CharField(max_length = 2048)
    option2 = models.CharField(max_length = 2048)
    option3 = models.CharField(max_length = 2048)
    option4 = models.CharField(max_length = 2048)
    answer = models.IntegerField()

class Submissions(models.Model):
    quizid = models.CharField(max_length = 10)
    name = models.CharField(max_length = 100)
    response = models.CharField(max_length = 2048)
    score = models.IntegerField()
    record_date = models.DateTimeField(auto_now_add = True)