from django.contrib import admin
from .models import NeighbourHood, User, Businesses

# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(User)
admin.site.register(Businesses)