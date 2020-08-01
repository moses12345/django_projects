from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact,About
from django.contrib import messages


#makemigration = identifing changes done in database
#migration = apply the changes done in make migration 
def index(request):
    contxt={
        "varia":"a"
    }
    return render(request,'index.html',contxt)
def about(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        about_you=request.POST.get('about_you')
        about=About(name=name,about_you=about_you,date=datetime.today())
        about.save()
        
    return render(request,'1.html')    

        
    
        
    
def contact(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        desc=request.POST.get('description')
        name=request.POST.get('name')
        contact=Contact(email=email,name=name,discription=desc,date=datetime.today())
        contact.save()
        messages.success(request,"your message has been sent {{contact.name}}")
        
    return render(request,'contact.html')
    #return HttpResponse("contact")    
