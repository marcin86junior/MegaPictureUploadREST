#python manage.py dumpdata imageupload --indent 4 > data.json
from pydoc import describe
from django.test import TestCase
from django.test import RequestFactory
from .models import UploadedImage
from .views import create_users
from imageupload_rest.views import UploadedImagesViewSet
from django.contrib.auth.models import User, Group

# Create your tests here.



'''
# models.py
class UploadedImageModelTestCase(TestCase):
    import os

    app_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    json_path = os.path.join(app_path, 'fixtures', 'data.json')
    fixtures = [json_path]
    fixtures = ['fdsfsfs']
    print('aaaaaaaaa')

    def setUp(self):
        User.objects.create_user('b1', '', '123') # user for Basic grup 
        User.objects.create_user('p2', '', '123') # user for Premium grup 
        User.objects.create_user('e3', '', '123') # user for Enterprise grup 
        User.objects.create_user('c4', '', '123') # user for Custom grup 
        login = self.client.login(username='b1', password='123') 
        self.assertTrue(login) 
        print("Oto obiekty usera 1: ", User.objects.get(id='1'))
        idx = User.objects.get(id='1')
        ''''
        UploadedImage.objects.create(image=(''), title='test',description='test', author = idx, duration='30')
        print(UploadedImage.objects.all())
        print(UploadedImage.objects.filter(pk='1'))
        request = RequestFactory().get('api/images/')
        print("get('api/ ................ ", request)
        request = RequestFactory().get('/api/images/?format=json/')
        print("get('/api/images/?format=json ................ ", request)
        print("Oto obiekty usera 1: ")

    def test_card_query(self):
        x= UploadedImage.objects.all()
        print(x)
        '''


'''
# views.py
class ImageListTestCase(TestCase):
    def test_bad_link(self):
        resp = self.client.get('/abcdefghijklmnoprstuwyz')
        self.assertEqual(resp.status_code, 404)
    def test_bad_pk(self):
        resp = self.client.get('api/Card/dsadsada')
        self.assertEqual(resp.status_code, 404)

    def test_get(self):
        request = RequestFactory().get('api/images/')
        view = UploadedImagesViewSet(actions={'get': 'get_user_agenda'})
        print("get('api/ ", request)
        print("view: ", view)


        pass
        response = view(request)
        print(response)
        self.assertEqual(response.status_code, 200)
'''
    
'''
    def test_get(self):
        request = RequestFactory().get('api/images/')
        view = UploadedImagesViewSet(actions={'get': 'get_user_agenda'})
        print("get('api/ ", request)
        print("view: ", view)
        response = view(request)
        print(response)
        self.assertEqual(response.status_code, 200)
'''
