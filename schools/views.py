from django.shortcuts import render
from .models import School

def school_list(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    district = request.GET.get('district', '')  # Фильтрация по району

    schools = School.objects.all()

    if query:
        schools = schools.filter(name__icontains=query)
    if category:
        schools = schools.filter(category=category)
    if district:
        schools = schools.filter(district=district)  # Фильтрация по району

    categories = {
        'public': 'Государственная',
        'private': 'Частная',
        'special': 'Специальная'
    }

    districts = {
        'central': 'Центральный район',
        'north': 'Северный район',
        'east': 'Восточный район',
        'west': 'Западный район',
        'south': 'Южный район'  # Добавлено южное направление
    }

    return render(request, 'schools/school_list.html', {
        'schools': schools,
        'categories': categories,
        'districts': districts,
        'query': query,
        'selected_category': category,
        'selected_district': district,
    })
