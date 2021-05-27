from rest_framework import routers, serializers, viewsets, status
from django.shortcuts import render
from .models import Language, Paradigm, Programmer
from .serializer import LanguageSerializer, ParadimSerializer, ProgrammerSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadimSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer


# ViewSets define the view behavior.

# from django.shortcuts import render 
# from school.models import Student
# from school.models import Teacher
# from django.http import HttpResponse 
# # Create your views here. 

# def index(request):
#     t = Teacher(name = "max", age = 41)
#     t.save()
#     objects = Student.objects.all().delete() 
#     student = Student(name = "Anupam", email = "anupam@journaldev.com",age = "24", section="A", Tname = str(t)) 
#     student.save() 
#     student = Student(name = "Another", email = "another@journaldev.com",age = "21", Tname = str(t)) 
#     student.save() 
#     objects = Student.objects.all() 
#     res ='Printing all Students entries in the DB : <br>'
#     for elt in objects: 
#         res += "Name:"+elt.name+"<br>"
#         res += "Age: "+ str(elt.age)+"<br>"
#         res += "Teachers name: " + str(elt.Tname)+"<br>"
#         res += "Section: "+ elt.section+"<br>"
#         res += "Section Full Name: "+elt.get_section_display()+"<br>"
        

#     return HttpResponse(res)
