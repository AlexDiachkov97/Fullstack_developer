from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Client

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('clients')
    else:
        form = LoginForm()
    return render(request, 'clients/login.html', {'form': form})

@login_required
def clients_view(request):
    clients = Client.objects.filter(responsible_person=request.user)
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        new_status = request.POST.get('status')
        client = Client.objects.get(account_number=client_id)
        client.status = new_status
        client.save()
    return render(request, 'clients/clients.html', {'clients': clients})

def logout_view(request):
    logout(request)
    return redirect('login')
