from django.urls import path
from django.conf import settings
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.upload_display_video, name='upload_display_video'),
    path('admin/', admin.site.urls),
    path('/submitted', views.submitted, name='submitted'),

]