from django.urls import path
from . import views 
# from django.contrib.auth import authenticate, login, logout

urlpatterns = [
    # path('welcome',views.welcome),   # welcome = url name  url Gonna Connect with Views
    # path('v1',views.v1),
    # path('Name/<user>',views.Name),
    # path('delete/<x1>/<x2>',views.delete),
    # path('add',views.add),
    # path('form',views.form),
    # path('html',views.html)
    # path('index',views.index)
    # path('contact',views.contact),
    # path('placement',views.placement)
    # path('create',views.create),
    # path('store',views.store),
    # path('date_time',views.date_time),
    # path('hello',views.hello),
    path('course',views.course),
    path('create_course',views.create_course),
    path('',views.get_course),
    path('delete/<int:rid>/',views.delete),
    path('edit/<int:rid>/',views.edit),
    path('filter_records',views.filter_records),
    path('showform',views.showform),
    path('signup',views.register),
    path('login',views.user_login, name = 'login'),
    path('profile',views.user_profile, name = 'profile'),
    path('logout',views.user_logout),
    path('set_cookie',views.set_cookie, name = 'set_cookie'),
    path('get_cookie',views.get_cookie, name = 'get_cookie'),
    path('del_cookie', views.del_cookie, name = 'del_cookie'),
    path('set_session',views.set_session, name = 'set_session'),
    path('get_session',views.get_session, name = 'get_session'),
    path('del_session',views.del_session, name = 'del_session'),
]