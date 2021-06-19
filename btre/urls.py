
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('pages.urls')), # Se pone la ruta del hompage
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
]
