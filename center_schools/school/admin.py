from django.contrib import admin

from .models import Person, Graduation

admin.site.register(Person)
admin.site.register(Graduation)
# admin.site.register(serializers.PersonSerializer)
