# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login/', views.user_login, name='login'),
# ]
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('EagleSoftware/templates/login.html', include('EagleSoftware.urls')),
]