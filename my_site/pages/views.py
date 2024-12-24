from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'pages/index.html')


def aboutus(request):
    return render(request, 'pages/aboutus.html')


def personalcab(request):
    return render(request, 'pages/personalcab.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('index')
            except Exception as e:
                # Обработка исключения
                print(f"Error: {e}")
                return render(request, 'pages/register.html', {'form': form, 'error': str(e)})
        else:
            return render(request, 'pages/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'pages/register.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to a different URL
    return render(request, 'pages/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
