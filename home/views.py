from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    context={
        "variable": "Dhruv Rathi is a Django Developer"
    }
    return render(request, 'index.html', context)
    # return HttpResponse('This is the home')
    
def home(request):
    context={
        "variable": "Dhruv Rathi is a Django Developer"
    }
    return render(request, 'home.html', context)
    # return HttpResponse('This is the homepage')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')
    # return HttpResponse('This is the services page')

def contact(request):
    return render(request, 'contact.html')
