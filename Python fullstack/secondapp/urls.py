
from django.urls import path
from . import views

urlpatterns=[
    # path('home/', views.home, name='secondpage'),
    path('page1/',views.secondpage,name='secondpage'),
    path('page2/',views.thirdpage,name='thirdpage'),
    path('photo/',views.photo,name='photo')
]