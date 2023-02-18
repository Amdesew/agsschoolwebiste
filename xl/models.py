from django.db import models

class New_Students(models.Model):
    full_name = models.CharField(max_length=100)
    wanted_class = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)

class Grade_Nine(models.Model):
    no = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    test_subjects = models.CharField(max_length=15)
    test_one = models.CharField(max_length=3)
    test_two = models.CharField(max_length=3)
    mid =  models.CharField(max_length=3)
    test_three = models.CharField(max_length=3)
    final = models.CharField(max_length=3)
    class Meta:
        db_table = 'Grade_Nine'

class Grade_Ten(models.Model):
    no = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    test_subjects = models.CharField(max_length=15)
    test_one = models.CharField(max_length=3)
    test_two = models.CharField(max_length=3)
    mid =  models.CharField(max_length=3)
    test_three = models.CharField(max_length=3)
    final = models.CharField(max_length=3)
    class Meta:
        db_table = 'Grade_Ten'

class Grade_Eleven(models.Model):
    no = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    test_subjects = models.CharField(max_length=15)
    test_one = models.CharField(max_length=3)
    test_two = models.CharField(max_length=3)
    mid =  models.CharField(max_length=3)
    test_three = models.CharField(max_length=3)
    final = models.CharField(max_length=3)
    class Meta:
        db_table = 'Grade_Eleven'

class Grade_Twelve(models.Model):
    no = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    test_subjects = models.CharField(max_length=15)
    test_one = models.CharField(max_length=3)
    test_two = models.CharField(max_length=3)
    mid =  models.CharField(max_length=3)
    test_three = models.CharField(max_length=3)
    final = models.CharField(max_length=3)
    class Meta:
        db_table = 'Grade_Twelve'