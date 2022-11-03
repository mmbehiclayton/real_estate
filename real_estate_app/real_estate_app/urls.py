
from django.contrib import admin
from django.urls import path

from listings.views import Listing_list, listing_retrieve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Listing_list),
    path('listings/<pk>', listing_retrieve)
]
