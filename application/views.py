from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def resume(request):
    return render(request, 'resume.html')

def services(request):
    return render(request, 'services.html')

def service_details(request):
    return render(request, 'services_details.html')


def portfolio_details(request):
    return render(request, 'portfolio_details.html')

def contact(request):
    return render(request, 'contact.html')
