from rest_framework import serializers
from .models import  Parent,Child,Place,ChildPlace


class ParentSeialiazer(serializers.ModelSerializer):
    Model=Parent
    fields=('pk','firstName','lastName','birthDate','photo')
class ChildSeialiazer(serializers.ModelSerializer):
    Model=Child
    fields=('pk','firstName','lastName','birthDate','photo','studyLevel','parent')
    