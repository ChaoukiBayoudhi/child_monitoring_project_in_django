from django.contrib import admin
from .models import Parent,Child,Place,ChildPlace
# Register your models here.
admin.site.register([Parent,Child,Place,ChildPlace])
#admin.site.register(Parent)
#admin.site.register(Parent)
