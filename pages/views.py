from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def donation(request):
    return render(request, 'pages/donation.html')
