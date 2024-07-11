from django.db import models

# Create your models here.

class QuizforMatric(models.Model):
    percentage=models.FloatField(verbose_name="Percentage")
    question1= models.CharField(verbose_name="Question No.1", max_length=50,null=True,blank=True)
    question2=models.CharField(verbose_name="Question No.2", max_length=50,null=True,blank=True)


class QuizforInter(models.Model):
    percentage=models.FloatField(verbose_name="Percentage")
    question1= models.CharField(verbose_name="Question No.1", max_length=50,null=True,blank=True)
    question2=models.CharField(verbose_name="Question No.2", max_length=50,null=True,blank=True)

