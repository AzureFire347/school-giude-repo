from django.contrib import admin
from .models import School

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'district', 'rating', 'google_maps_url')  # Добавляем поле district в список
    search_fields = ('name', 'address')  # Оставляем возможность поиска по имени и адресу
    list_filter = ('category', 'district')  # Фильтруем по категории и району

    # Добавим это поле в формы редактирования
    fields = ('name', 'address', 'contact_info', 'description', 'rating', 'category', 'district', 'image', 'google_maps_url')  # Добавляем district
