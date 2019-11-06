from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:id>', views.detail, name='detail'),
    path('result/<int:id>', views.result, name='result'),
    path('vote/<int:id>', views.vote, name='vote')
]