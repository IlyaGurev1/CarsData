from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='Главная страница'),
    path('news', views.News.as_view()),
    path('about', views.About.as_view())
]