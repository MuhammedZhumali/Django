from django.db.models import fields
from .models import Language, Paradigm, Programmer
from rest_framework import serializers

# Serializers define the API representation.
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields=('id', 'url', 'name', 'paradigm')
    
class ParadimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields=('id', 'url', 'name')

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'url', 'name', 'language')