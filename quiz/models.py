from django.db import models
from accounts.models import User
import uuid
from django.urls import reverse


class Category(models.Model):
    
    id = models.UUIDField( primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255)
    

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('quiz_view', kwargs={ 'id':self.id })
    
    def get_category_url(self):
        return reverse('category_detail', kwargs={ 'id':self.id })
class Student(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null= True, blank=True,)

    def __str__(self):
        return self.user.email

class Question(models.Model):

    id = models.UUIDField(primary_key=True,editable=False, default=uuid.uuid4, unique=True)
    student = models.ForeignKey( Student , on_delete=models.CASCADE,null= True, blank=True,)
    # question_number   = models.PositiveIntegerField(primary_key=True,unique=False)
    full_question     = models.TextField()
    correct_answer    = models.OneToOneField('Option' , on_delete=models.CASCADE , related_name='correct_ans' , null= True , blank=True )
    category          = models.ForeignKey( Category , on_delete=models.CASCADE,null= True, blank=True,)
   
    def __str__(self) -> str:
        return self.full_question

class Option(models.Model):

    id = models.UUIDField( primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    option_txt = models.CharField(max_length=255)
    question   = models.ForeignKey(Question , on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.option_txt
class ScoreCard(models.Model):

    id = models.UUIDField( primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.IntegerField()
    category     = models.ForeignKey( Category , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.category.name



