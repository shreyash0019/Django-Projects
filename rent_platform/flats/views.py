from django.shortcuts import render
from .models import Property
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    properties = Property.objects.filter(is_available=True)
    return render(request, 'home.html', {'properties': properties})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def add_property(request):
    # Only authenticated users can add properties
    if request.user.role != 'landlord':
        return redirect('home')  # Redirect to home if not a landlord
    
    # Your property creation logic here
    return render(request, 'add_property.html')