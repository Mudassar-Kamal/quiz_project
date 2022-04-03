from django.db import models
from accounts.models import User
import uuid

# Create your models here.

class Student(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class QuizQuestion(models.Model):
    student = models.ForeignKey(Student, null= True, blank=True, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    correct_ans = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(QuizQuestion, related_name="choices", on_delete=models.CASCADE)
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice

class Result(models.Model):
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)



