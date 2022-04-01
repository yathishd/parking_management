#imported
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import locationclass
from django.views.generic import TemplateView,ListView

#home page
class HomeView(TemplateView):
    template_name='index.html'
    
#All parking locations
class Allparking(ListView):
    template_name='allparking.html'
    queryset=locationclass.objects.all()
    context_object_name='allparking_objects'

#search function
def searchfunction(request):
    slot_objects=locationclass.objects.all()
    
    #search function
    slot_name=request.GET.get('slot_name')
    if slot_name!="" and slot_name is not None:
        slot_objects=locationclass.objects.filter(location_name__icontains=slot_name)
        return render(request,'searchresult.html',{'slot_objects':slot_objects})
    else:
        messages.warning(request,"please enter location")
        return redirect('home-page')
    
    
#imported 
from django.contrib.auth.models import User

#sign up function
def signupfunction(request):
    if request.method == 'POST':
        #firstname is any variable & Fname is "name" value from form we accessing it as dictionary key here
        username=request.POST['username']
        firstname=request.POST['Fname']
        lastname=request.POST['Lname']
        email=request.POST['email']
        password=request.POST['password']
        
        #creating user
        myuser =User.objects.create_user(username=username,email=email,password=password)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        messages.success(request, 'Your account is created -Now you can Login')
        return redirect('home-page')
        
    else:
        messages.warning(request,"not allowed without proper details")   

#imported 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#login function
def loginfunction(request):
    #loginemail=request.POST['loginemail']  
    loginusername=request.POST.get('loginusername')
    loginemail=request.POST.get('loginemail')
    #loginpassword=request.POST['loginpassword']  
    loginpassword=request.POST.get('loginpassword')
    
    user = authenticate(username=loginusername,email=loginemail, password=loginpassword)
    
    if user is not None:
        login(request, user) #user is above variable
        messages.success(request, 'login is successfull...Now you can book parking')
        return redirect('all-parking') 
    else:
        messages.warning(request, 'Enter correct email and password')
        return redirect('all-parking')
    
#logout function 
def logoutfunction(request):  
    logout(request)
    messages.info(request, 'you have logged out')
    return redirect('all-parking')
