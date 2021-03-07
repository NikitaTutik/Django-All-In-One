from django.urls import path
from .views import mainview, mainpage

urlpatterns = [
    path('shorturl/', mainview, name='mainurl'),
    path('', mainpage, name='mainpage')
]
