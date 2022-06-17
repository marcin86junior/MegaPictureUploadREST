from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group

def create_group(abc):
    user, created = Group.objects.get_or_create(name=abc)
    user.save()
create_group('Basic')
create_group('Premium')
create_group('Enterprise')
create_group('Custom')

def create_users(request):
    def create_user(abc, bcd):
        user, created = User.objects.get_or_create(username=abc)
        user.set_password('123')
        my_group = Group.objects.get(name=bcd) 
        my_group.user_set.add(user)
        user.save()
    create_user('b1', 'Basic')
    create_user('p2', 'Premium')
    create_user('e3', 'Enterprise')
    create_user('c4', 'Custom')
    return HttpResponse('<b>User/pass and groups created: </b><br>\
        b1 (pass:123) --> Basic group <br>\
        p2 (pass:123) --> Premium group <br>\
        e3 (pass:123) --> Enterprice group <br>\
        c4 (pass:123) --> Custom group')