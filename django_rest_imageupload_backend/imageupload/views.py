from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group

def create_users(request):
    def create_user(abc):
        user, created = User.objects.get_or_create(username=abc)
        user.set_password('123')
        user.save()
    create_user('tomek')
    create_user('premium')
    create_user('enterprice')

    def create_group(abc):
        user, created = Group.objects.get_or_create(name=abc)
        user.save()
    create_group('Basic')
    create_group('Premium')
    create_group('Enterprise')
    create_group('CustomXX500x500')
    return HttpResponse('Users and groups created: \n Maciej(pass:123) -> Basic group \n Pawel(pass:123) -> Premium group \n Jacek(pass:123) -> Enterprice group')