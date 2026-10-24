from django.contrib import admin
from django.urls import path, include
from apps.views import home, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls')),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
]