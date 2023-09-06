from django.db import models

# Create your models here.
from datetime import datetime

# class LaptopModels(models.Model):
#     name = models.CharField(max_length=25,default='mac')
#     price = models.PositiveIntegerField(default=1)
#     ram  = models.PositiveSmallIntegerField(default=1)

#     class Meta:
#         db_table = 'polls_laptop'

class Question(models.Model):
    question_text = models.CharField(max_length=200,default='')
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.question_text
    
    class Meta:
        db_table = 'polls_question'

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    class Meta:
        db_table = 'polls_choice'