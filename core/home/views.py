from django.shortcuts import render
from django.http import HttpResponse

def homie(request):
   
   vegetable = [{
        'x': 'potato',
        'y': 'carrot',
        'z': 'onion'
    }]
   return render(request, 'home/index.html', context={ 'vegetable':vegetable,'pages':'home'})

def about(request):
   peoples=[
      {'name': 'Django', 
    'age': 3, 
    'hobby': 'coding'
    },
     { 'name':'Bigyan Luitel',
      'age':22,
      'hobby':'coding'
      },
      {'name':'Sanjay Luitel',
      'age': 25,
      'hobby':'coding'
      }]
   return render(request,'home/about.html', context={'peoples':peoples,'pages':'about'})
def contact(request):
   return render(request,'home/contact.html', context={'pages':'contact'})

