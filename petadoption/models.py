from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='animal_images/')

    def __str__(self):
        return self.name

class Adopter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Adoption(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE)
    adoption_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.animal.name} adopted by {self.adopter.name} on {self.adoption_date}'

class Animals_List(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
        

def animal_list(request):
    # Fetch all Animal objects from the database
    animals = Animal.objects.all()
    
    # Pass the retrieved data to the animal_list.html template
    return render(request, 'petadoption/animal_list.html', {'animals': animals})
    