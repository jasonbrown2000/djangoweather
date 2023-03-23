from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def calculator(request):
    if request.method == 'POST':
        beers = request.POST.get('beers')
        wines = request.POST.get('wines')
        spirits = request.POST.get('spirits')
        ciders = request.POST.get('ciders')
        
        # Calculate the total number of units
        total_units = (float(beers)*2) + (float(wines)*2.5) + (float(spirits)*1) + (float(ciders)*2)
        
        # Calculate the total number of calories
        total_calories = (float(beers)*140) + (float(wines)*85) + (float(spirits)*64) + (float(ciders)*239)
        
        return render(request, 'result.html', {'total_units': total_units, 'total_calories': total_calories})

    else:
        # code to handle GET requests
        return render(request, 'calculator.html')

    

