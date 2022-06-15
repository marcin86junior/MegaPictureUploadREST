#python manage.py dumpdata imageupload --indent 4 > data.json
from django.test import TestCase
from django.test import RequestFactory
from .models import UploadedImage
from .views import create_users

#from .models import Card, Dish, CardItems
#from .views import CardView

# Create your tests here.

# models.py
class CardModelTestCase(TestCase):
    fixtures = ['data.json']
    def setUp(self):
        Card.objects.create(name="Testowa karta", description="Karta utworzona do testow")
        Dish.objects.create(name="Danie testowe", description="Danie utowrzone do testów", price='15', preparation_time='15')
        card = Card.objects.get(name="Testowa karta")
        dish = Dish.objects.get(name="Danie testowe")
        CardItems.objects.create(card_id = dish.id, dish_id = dish.id)
    def test_card_query(self):
        card = Card.objects.get(name="Testowa karta")
        self.assertEqual(card.description, 'Karta utworzona do testow')

# views.py
class CardListTestCase(TestCase):
    def test_get(self):
        request = RequestFactory().get('/lista/')
        view = CardView.as_view()
        response = view(request)
        #print(response)
        self.assertEqual(response.status_code, 200)
    def test_bad_link(self):
        resp = self.client.get('/abcdefghijklmnoprstuwyz')
        self.assertEqual(resp.status_code, 404)
    def test_bad_pk(self):
        resp = self.client.get('api/Card/dsadsada')
        self.assertEqual(resp.status_code, 404)


