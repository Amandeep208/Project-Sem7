from django.contrib import admin

# Register your models here.
from .models import Food, Exercise

# Register the Food and Exercise models to the admin site
admin.site.register(Food)
admin.site.register(Exercise)
