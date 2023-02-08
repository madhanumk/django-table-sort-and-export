from django.contrib import admin
from .models import Student,Country, State, Grade
# Register your models here.


admin.site.register(Student)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Grade)