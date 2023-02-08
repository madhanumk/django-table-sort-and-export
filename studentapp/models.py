from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Grade(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


gender_options = (('','Choose Gender'),('M','Male'),('F','Female'))
section_options = (('','Choose Section'),('A','A'),('B','B'),('C','C'),('D','D'))


class Student(models.Model):    
    name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50,unique=True)
    age = models.IntegerField()
    gender = models.CharField(choices=gender_options,max_length=1)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE)
    section = models.CharField(choices=section_options,max_length=1)


    def __str__(self):
        return self.name



    class Meta:
        ordering = ['name']

