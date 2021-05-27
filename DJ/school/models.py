from django.db import models # Create your models here. 

class Paradigm(models.Model):
    name = models.CharField(max_length=50)

def __str__(self):
    return self.name     

class Language(models.Model):
      name = models.CharField(max_length=50)
      paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)
def __str__(self):
        return self.name
    
class Programmer(models.Model):
    name = models.CharField(max_length=50)
    language = models.ManyToManyField(Language)
def __str__(self):
        return self.name

# class Student(models.Model): 
#     SECTION = ( ('A', 'Alpha'), ('B', 'Beta'), ('C', 'Cappa'), )
#     name = models.CharField(max_length=30) 
#     age = models.IntegerField() 
#     email = models.EmailField()
#     section = models.CharField(max_length=1, choices=SECTION, 
#     default=SECTION[1][0])
#     Tname=models.CharField(max_length=30, default='BRRR')

# class Teacher(models.Model):
#     name = models.CharField(max_length=30) 
#     age = models.IntegerField() 