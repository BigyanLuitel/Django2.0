from django.shortcuts import render,redirect
from .models import recipie

# Create your views here.
def recepies(request):
    if request.method=="POST":
        data=request.POST
        recepie_name=data.get('recepie_name')
        recepie_description=data.get('recepie_description')
        recepie_image=request.FILES.get('recepie_image')
        print(recepie_name,recepie_description,recepie_image)
        
        recipie.objects.create(
            recepie_name=recepie_name,
            recepie_description=recepie_description,
            recepie_image=recepie_image
        )
       
        return redirect('/recepies/')
    queryset=recipie.objects.all()
    context={
            'pages':'recepies',
            'recepies':queryset
        }
    return render(request,'veggie/recepies.html', context)

def delete_recepies(request, id):
    if request.method == "POST":
        data = recipie.objects.get(id=id)
        data.delete()
    return redirect('/recepies/')

def update_recepies(request, id):
    data = recipie.objects.get(id=id)  
    if request.method=="POST":
        querySet=request.POST
        recepie_name=querySet.get('recepie_name')
        recepie_description=querySet.get('recepie_description')
        recepie_image=request.FILES.get('recepie_image')
        
        data.recepie_name=recepie_name
        data.recepie_description=recepie_description
        if recepie_image:
            data.recepie_image=recepie_image
        
        data.save()
        return redirect('/recepies/')
        
    context = {'recepie': data}
    return render(request, 'veggie/update.html', context)
