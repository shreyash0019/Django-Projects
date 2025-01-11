from django.shortcuts import render
from datetime import datetime

def info_view(request):
    current_time = datetime.now()
    course_info = {
        'name': 'Django',
        'prerequisite': 'Python',
        'students': [  # Replace with actual student data retrieval logic
            {'name': 'Alice', 'feedback': 'Good'},
            {'name': 'Bob', 'feedback': 'Excellent'},
        ],
    }
    return render(request, 'tsetapp/results.html', context=course_info)