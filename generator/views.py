from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
	#return HttpResponse('<h1>Hello there buddy<h1>')
	return render(request,'generator/home.html',{'password':'as3213'})

def password(request):
	
	thepassword=''

	characters = list('abcdefghijklmnopqrstuvwyz')
	length=int(request.GET.get('length',12))
	
	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		characters.extend(list('!@$%&*()'))	

	for x in range(length):
		thepassword=thepassword + random.choice(characters)

	return render(request,'generator/password.html',{'password':thepassword})