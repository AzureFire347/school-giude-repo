from django.urls import path
from .views import school_list  # Проверь, что этот импорт существует

urlpatterns = [
    path('', school_list, name='school_list'),  # Добавь хотя бы один маршрут
]
