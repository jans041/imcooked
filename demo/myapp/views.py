from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.

def home(request):
    return render(request, "home.html") 

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", { "todos":items})

def submit_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname') #this saves the fname in the html file to first_name
        last_name = request.POST.get('lname') #same but for last name
        print(f'First Name: {first_name}, Last Name: {last_name}')