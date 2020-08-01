from django.shortcuts import render,HttpResponse,redirect
from .forms import Createforms
from .models import Poll

# Create your views here.

def home(request):
    poll=Poll.objects.all()

    context={
        'polls':poll
    }
    return render(request,'home.html',context)

def create(request):
    if request.method=="POST":
        form=Createforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Createforms()    
    context={
        'form':form
    }
    return render(request,'create.html',context)
def vote(request,poll_id):
    poll=Poll.objects.get(pk=poll_id)
    if request.method=="POST":
        selected=request.POST['poll']
        print(selected)
        if selected=="option1":
            poll.option1_counts+=1
        elif selected=="option2":
            poll.option2_counts+=1
        elif selected=="option3":
            poll.option3_counts+=1
        else:
            return HttpResponse(400,"choice one")
        poll.save()

        return redirect('result',poll.id )       
            


    context={
        'poll':poll
    }
    return render(request,'vote.html',context)
def result(request,poll_id):
    polls=Poll.objects.get(pk=poll_id)
    context={
        'poll':polls
    }
    return render(request,'result.html',context)        
