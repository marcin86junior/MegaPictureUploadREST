from .models import UploadedImage

from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.test import RequestFactory
from django.utils import timezone

from imageupload.models import UploadedImage
from imageupload_rest.views import UploadedImagesViewSet

# group test
class GroupTest(TestCase):
    fixtures = ["group.json"]

    def test_of_group_fixtures(self):
        group = Group.objects.get(pk=1)
        self.assertEqual(group.name, "Basic")

# user test
class UserTest(TestCase):
    fixtures = ["users.json", "group.json"]

    def test_of_user_fixturs(self):
        user = User.objects.get(pk=1)
        self.assertEqual(str(user), "b1")

    def test_login_basic_user_with_correct_password(self):
       login = self.client.login(username='b1', password='123')
       self.assertTrue(login) 
    
    def test_login_basic_user_with_wrong_password(self):
       login = self.client.login(username='b1', password='1234')
       self.assertFalse(login) 

# model
class ModelsTestCase(TestCase):
    fixtures = ['data.json', 'users.json', 'group.json']

    def test_uploadedImage_model_without_piture_file(self):
        login = self.client.login(username='b1', password='123') 
        uploadedImage = UploadedImage.objects.create(author=User.objects.get(id=1), title="My first post")
        uploadedImage.save()
        self.assertEqual(uploadedImage.title, 'My first post')

    def test_uploadedImage_model_with_piture_file(self):
        login = self.client.login(username='b1', password='123') 
        try:
            imagex = SimpleUploadedFile(name='123.jpg', content=open('./abc.jpg', 'rb').read(), content_type='image/jpeg')
        except:
            image_path = ('')
        uploadedImage = UploadedImage.objects.create(
            author=User.objects.get(id=1),
            description='Test description',
            title='Test name',
            create_date=timezone.now(),
            image=imagex,
            duration=60,
        )
        uploadedImage.save()
        self.assertEqual(uploadedImage.title, 'Test name')

# views.py
class ViewsTestCase(TestCase):
    fixtures = ['data.json', 'users.json', 'group.json']
 
    def setUp(self):
        self.logged_in = self.client.login(username='b1', password='123')
        login = self.client.login(username='b1', password='123') 
        self.assertTrue(login) 
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

from rest_framework.test import APIRequestFactory

class ViewsTestCase(TestCase):
    fixtures = ['data.json', 'users.json', 'group.json']

    def setUp(self):
        self.logged_in = self.client.login(username='b1', password='123')
        login = self.client.login(username='b1', password='123') 
        self.assertTrue(login) 

    # Using the standard RequestFactory API to create a form POST request
    factory = APIRequestFactory()
    request = factory.post('/notes/', {'title': 'new idea'})

    def test_index_loads_properly(self):
        """The '' page should be 404"""
        request = RequestFactory().get('api/images/')
        request = RequestFactory().get('/api/images/?format=json/')
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 404)

'''
request = RequestFactory().get('api/images/')
request = RequestFactory().get('/api/images/?format=json/')

#we can also create super user
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
        xxx
'''