from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import AnimalForm, RegistrationForm
from .models import Animal, Animals_List

def home(request):
    return render(request, 'petadoption/home.html')

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'petadoption/animal_detail.html', {'animal': animal})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'petadoption/admin_login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'petadoption/admin_login.html')

def animals_list(request):
    # Retrieve all animal objects from the database
    animals = Animal.objects.all()
    # Pass the animals data to the template
    return render(request, 'petadoption/animals_list.html', {'animals_data': animals})
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'petadoption/register.html', {'form': form})

@login_required
def admin_dashboard(request):
    animals = Animal.objects.all()
    return render(request, 'petadoption/admin_dashboard.html', {'animals': animals})

def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animals_list')
    else:
        form = AnimalForm()
    return render(request, 'petadoption/add_animal.html', {'form': form})

def edit_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'petadoption/edit_animal.html', {'form': form})

def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if request.method == 'POST':
        animal.delete()
        return redirect('admin_dashboard')
    return render(request, 'petadoption/delete_animal.html', {'animal': animal})
    
@login_required
def dashboard(request):
    return render(request, 'petadoption/dashboard.html')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the dashboard or any other desired page after successful login
            return redirect('/dashboard/')  # Assuming 'dashboard' is the name of your dashboard URL
        else:
            # If authentication fails, display an error message
            error = 'Invalid username or password'
            return render(request, 'login.html', {'error': error})
    else:
        # If it's a GET request, render the login form
        return render(request, 'login.html')

