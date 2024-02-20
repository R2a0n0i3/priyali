from django.shortcuts import render

def index(request):
    return render(request, 'DeliciousApp/index.html')
def login(request):
    return render(request, "DeliciousApp/login.html")
# Create your views here.

def my_view(request):
    # Your view logic goes here
    context = {
        'variable': 'value',  # Pass any context variables you want to use in the template
    }
    return render(request, 'myapp/my_t'
                           'emplate.html', context)