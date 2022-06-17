#python manage.py dumpdata imageupload --indent 4 > data.json
from django.test import TestCase
from django.test import RequestFactory
from .models import UploadedImage
from imageupload_rest.views import UploadedImagesViewSet
from django.contrib.auth.models import User, Group
from django.template.defaultfilters import slugify
from imageupload.models import UploadedImage


# group test
class GroupTest(TestCase):
    fixtures = ["group.json"]

    def test_should_create_group(self):
        group = Group.objects.get(pk=1)
        self.assertEqual(group.name, "Basic")

'''
class ViewTests(TestCase):
    """
    Run before each test in class
    """
    fixtures = ['data.json']

    def setUp(self):
        self.user = User.objects.create_superuser(
            'marcin',
            '',
            '123'
        )
        self.logged_in = self.client.login(
            username='marcin',
            password='123'
        )

    """
    Test whether user can login and post choice
    to db and then check if data can be retreived.
    """
    def test_card_query(self):
        uploadedImage = UploadedImage.objects.all()
        firstpicture = uploadedImage.objects.get(author=User.objects.get(pk=1))
        self.assertEqual(card.description, 'Karta utworzona do testow')
'''


# user test
class UserTest(TestCase):
    fixtures = ["users.json"]
    #fixtures = ["group.json"]

    def test_should_load_user_from_fixture(self):
        user = User.objects.all().filter(User='1')

        self.assertEqual(str(user), "b1")
'''

    def test_should_create_user(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        self.assertTrue(login) 
'''


'''

# model
class ModelsTestCase(TestCase):
    fixtures = ['data.json']

    def test_uploadedImage_has_slug(self):
        login = self.client.login(username='b1', password='123') 
        self.assertTrue(login) 
        uploadedImage = UploadedImage.objects.get(pk=1)
        self.assertEqual(uploadedImage, "x")
'''

'''
    def test_uploadedImage_has_slug(self):
        """Posts are given slugs correctly when saving"""
        uploadedImage = UploadedImage.objects.create(title="My first post", author='User.')

        uploadedImage.author = "b1"
        uploadedImage.save()
        self.assertEqual(uploadedImage.slug, slugify(uploadedImage.title))
'''


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
        self.assertEqual(response.status_code, 200)
    def test_bad_link(self):
        resp = self.client.get('http://127.0.0.1:8000/media/xxx.PNG')
        self.assertEqual(resp.status_code, 404)
    def test_bad_pk(self):
        resp = self.client.get('api/Users/1')
        self.assertEqual(resp.status_code, 404)


'''
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

