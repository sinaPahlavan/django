from django.urls import path
from django.conf import settings
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('admin/', admin.site.urls),
    path('privacy/',admin.site.urls),
    path('termsAndConditions/',admin.site.urls),
    path('contact/',views.contact, name = 'contact'),
    #path('submitted/', views.submitted, name='submitted'),

]