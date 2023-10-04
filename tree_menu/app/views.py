from django.shortcuts import render

def contacts_view(request):
    return render(request, 'contacts.html')

def about_view(request):
    return render(request, 'about.html')

def home_view(request):
    return render(request, 'home.html')
