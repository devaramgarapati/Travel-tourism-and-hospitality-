from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def secondpage(request):
    return HttpResponse('<h1><center>This is printing from second page</center></h1>')
# def durgaprasad(request):
#     return HttpResponse('<h1><center>printing from app1</center></h1>')
def thirdpage(request):
    return HttpResponse('<h1><center>This is printing from third page</center></h1>')
def photo(request):
    return render('request','photo.html')


