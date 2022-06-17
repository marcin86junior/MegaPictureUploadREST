#python manage.py dumpdata imageupload --indent 4 > data.json
from pydoc import describe
from django.test import TestCase
from django.test import RequestFactory
from .models import UploadedImage
from .views import create_users
from imageupload_rest.views import UploadedImagesViewSet
from django.contrib.auth.models import User, Group

# Create your tests here.

# group test
class GroupTest(TestCase):
    fixtures = ["group.json"]

    def test_should_create_group(self):
        group = Group.objects.get(pk=1)
        self.assertEqual(group.name, "Basic")

# views.py
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The '' page should be 404"""
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 404)
    def test_index_loads_properly2(self):
        """The api/ page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/api/')
        self.assertEqual(response.status_code, 200)
    def test_index_loads_properly2(self):
        """The api/images/ page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/api/images/')
    def test_bad_link(self):
        resp = self.client.get('http://127.0.0.1:8000/media/xxx.PNG')
        self.assertEqual(resp.status_code, 404)
    def test_bad_pk(self):
        resp = self.client.get('api/Users/1')
        self.assertEqual(resp.status_code, 404)


'''

from django.template.defaultfilters import slugify
from imageupload.models import UploadedImage


class ModelsTestCase(TestCase):
    def test_uploadedImage_has_slug(self):
        """Posts are given slugs correctly when saving"""
        uploadedImage = UploadedImage.objects.create(title="My first post")

        uploadedImage.author = "1"
        uploadedImage.save()
        self.assertEqual(uploadedImage.slug, slugify(uploadedImage.title))
'''


'''

# user test
class UserTest(TestCase):
    fixtures = ["users.json"]

    def test_should_create_user(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, "b1")

    def test_should_check_password(db) -> None:
        user = User.objects.create_user("A")
        user.set_password("secret")
        assert user.check_password("secret") is True

    def test_should_not_check_unusable_password(db) -> None:
        user = User.objects.create_user("A")
        user.set_password("secret")
        user.set_unusable_password()
        assert user.check_password("secret") is False

''''''
# models.py
class CardModelTestCase(TestCase):
    fixtures = ['/imageupload/data.json']
    def setUp(self):
        login = self.client.login(username='b1', password='123') 
        self.assertTrue(login) 


        UploadedImage.objects.create(image=(''), title='test',description='test', author = idx, duration='30')
        print(UploadedImage.objects.all())
        print(UploadedImage.objects.filter(pk='1'))
        request = RequestFactory().get('api/images/')
        print("get('api/ ................ ", request)
        request = RequestFactory().get('/api/images/?format=json/')
        print("get('/api/images/?format=json ................ ", request)
        print("Oto obiekty usera 1: ")

        Card.objects.create(name="Testowa karta", description="Karta utworzona do testow")
        Dish.objects.create(name="Danie testowe", description="Danie utowrzone do testów", price='15', preparation_time='15')
        card = Card.objects.get(name="Testowa karta")
        dish = Dish.objects.get(name="Danie testowe")
        CardItems.objects.create(card_id = dish.id, dish_id = dish.id)
    def test_card_query(self):
        card = Card.objects.get(name="Testowa karta")
        self.assertEqual(card.description, 'Karta utworzona do testow')

'''

