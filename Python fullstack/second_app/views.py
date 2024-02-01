from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate

# Create your views here.
from django.http import HttpResponse
from . import templates
# from .models import tb1_auth


def second_page(request):
    return HttpResponse('<body><center><h1>this is from second_app akhil page1</h1></center></body>')
def login(request):
    return render(request,'second_app/logintoday.html')
def signin(request):
    # if request.method=='POST':
    #     fname=request.POST.get('fname')
    #     lname = request.POST.get('lname')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     try:
    #         user=tb1_auth.tth_ob.get(fname=fname,lname=lname,email=email,password=password)
    #         if user is not None:
    #             return render(request,'main.html',{})
    #         else:
    #             print('sigin in failed')
    #
    #             return redirect('/')
    #     except Exception as identifier:
    #         return redirect('/')
    # else:
    #     return render(request,'logintoday.html')


    return render(request,'second_app/signup.html')
def about(request):
    return render(request,'second_app/about.html')
def mainpage(request):
    return render(request,'second_app/main.html')

