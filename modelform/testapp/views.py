from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.
def Student_view(request):
    #form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    form = StudentForm()
    return render(request, 'testapp/index.html', {'form': form})
    
