from django.urls import path
from .views import school_list  # Импортируем представление для списка школ

urlpatterns = [
    path('', school_list, name='school_list'),  # Главная страница будет отображать список школ
]
