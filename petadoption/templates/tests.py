from django.test import TestCase, Client
from django.urls import reverse
from .models import Animal

class AnimalTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.animal = Animal.objects.create(name='Test Animal', species='Dog', age=3)

    def test_animal_list_view(self):
        response = self.client.get(reverse('animal_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.animal.name)

    def test_animal_detail_view(self):
        response = self.client.get(reverse('animal_detail', args=[self.animal.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.animal.name)
