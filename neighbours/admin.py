from django.contrib import admin
from .models import NeighbourHood, User, Businesses, Posts

# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(User)
admin.site.register(Businesses)
admin.site.register(Posts)