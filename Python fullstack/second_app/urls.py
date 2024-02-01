from django.urls import path
from . import views

from django.urls import path,include

urlpatterns = [path('page1/', views.second_page, name='second_app'),
               path('login/',views.login,name='login'),
               path('siginin/',views.signin,name='signin'),
               path('about/', views.about, name='about'),
               path('main/', views.mainpage, name='main')
               ]
