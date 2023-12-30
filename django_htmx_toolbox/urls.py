from django.contrib import admin
from django.urls import path, include

from test_htmx_widgets.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('widgets/', include('widgets.urls')),
    path('home', home, name='home'),
]
