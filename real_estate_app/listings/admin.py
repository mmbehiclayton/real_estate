from django.contrib import admin
from .models import Listing

# Register your models here.
admin.site.register(Listing)

#change admin site header
admin.site.site_header = "Real Estate App Admin"