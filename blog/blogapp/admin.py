from django.contrib import admin
from .models import Category, Blog

#Register the model in admin interface
admin.site.register(Category)
admin.site.register(Blog)
