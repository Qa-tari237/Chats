from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import OmboliSignup
from .models import Omboli_Room
from .models import OmboliMessage

# Create your views here.
def omboli_frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form= OmboliSignup(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form= OmboliSignup()

    return render(request, 'core/signup.html',{'form': form})

def logout_view(request):
    """
    Logs out the user and redirects to the login page.
    """
    logout(request)
    return redirect('login')


@login_required
def rooms(request):
    rooms= Omboli_Room.objects.all()

    return render(request, 'core/rooms.html',{'rooms': rooms})

@login_required
def room(request, slug):
    room = Omboli_Room.objects.get(slug=slug)
    messages = OmboliMessage.objects.filter(room=room)[0:25]

    return render(request, 'core/room.html',{'room': room, 'messages':messages})