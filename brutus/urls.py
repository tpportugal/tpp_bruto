from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('browser/', views.browser, name='browser'),
    path('contributors/', views.contributors, name='contributors'),
    path('become-contributor', views.become_contributor, name='become-contributor')
]
