from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rus_slov', views.rus_slov, name='rus_slov'),
    path('slov_rus', views.slov_rus, name='slovrus'),
]