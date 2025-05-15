from django.shortcuts import render,redirect,get_object_or_404
from veggie.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Sum

@login_required(login_url="/login_page/")
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
    
    if request.GET.get('Search'):
        queryset=queryset.filter(recepie_name__icontains=request.GET.get('Search'))
        
    context={
            'pages':'recepies',
            'recepies':queryset
        }
    return render(request,'veggie/recepies.html', context)

def delete_recepies(request, id):
    if request.method == "POST":
        data = get_object_or_404(recipie, id=id)
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

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist.')
            return redirect('/login_page/')
        user=authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, 'Invalid username or password.')
            return redirect('/login_page/')
        else:
            login(request,user)
            return redirect('/recepies/')
    return render(request, 'veggie/login.html', context={'pages': 'login'})
def logout_page(request):
    logout(request)
    return redirect('/login_page/')
    
def register(request):
    if request.method== "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'veggie/register.html', {
                'pages': 'register'
            })
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        user.set_password(password)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('/login_page/')
    
    return render(request, 'veggie/register.html', context={'pages':'register'})



def get_student(request):
    queryset=Student.objects.all()
    ranks=queryset.annotate(marks=Sum('student_marks__marks')).order_by('-marks','-student_age')
    print(ranks)
    if request.GET.get('search'):
        queryset=queryset.filter(
            Q(student_name__icontains=request.GET.get('search'))|
            Q(student_email__icontains=request.GET.get('search'))|
            Q(student_address__icontains=request.GET.get('search'))|
            Q(student_id__student_id__icontains=request.GET.get('search'))|
            Q(Department__department__icontains=request.GET.get('search'))
        )
    paginator = Paginator(queryset, 25)  
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    
    return render(request,'veggie/student.html',context={
        'pages':'student',
        'students':page_obj,
    })
from veggie.seed import generate_report_card
def see_marks(request,student_id):
    generate_report_card(student_id)
    queryset = subjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks=queryset.aggregate(total_marks=Sum('marks'))
    current_rank=-1
    ranks=Student.objects.annotate(marks=Sum('student_marks__marks')).order_by('-marks','-student_age')
    i=1
    for rank in ranks:
        if rank.student_id.student_id==student_id:
            current_rank=i
            break
        i=i+1
    return render(request,'veggie/see_marks.html',context={
        'pages':'see_marks',
        'marks':queryset,
        'total':total_marks,
        'current_rank':current_rank
    })