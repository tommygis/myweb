from django.contrib import admin

from blog.models import Person, News
# Register your models here.

admin.site.register(Person)
admin.site.register(News)
