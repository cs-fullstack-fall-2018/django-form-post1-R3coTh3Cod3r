from django.urls import path
from . import views




urlpatterns = [
    path('name/', views.name, name='Name '),
    path('genre/', views.genre, name='Genre')
]