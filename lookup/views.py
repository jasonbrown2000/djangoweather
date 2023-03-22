from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def calculator(request):
	return render(request, 'calculator.html', {})

