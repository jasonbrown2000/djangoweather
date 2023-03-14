from django.shortcuts import render

def home(request):
	# To add API
	# import json
	# import requests

	# api_request = requests.get("https://api.catalog.beer/beer")
	# My API : b708854d-bd90-4663-a11c-587f88422f67
	# Website Tutorial : https://catalog.beer/api-docs#beer-list-all

	# try:
		# api = json.loads(api_request.content)
	# except Exception as e:
		# api = 'Error..'

	# Add 'api': api in between {} below
	return render(request, 'home.html', {})

def calculator(request):
	return render(request, 'calculator.html', {})

