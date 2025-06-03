from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'accounts/register.html', {'form': form, 'errors': form.errors})
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})





@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


def logout(request):
    return render(request, 'accounts/logout.html')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

def main(request):
    return render(request, 'accounts/main.html')

def history(request):
    return render(request, 'accounts/history.html')

def fleet(request):
    return render(request, 'accounts/Fleet.html')
def base(request):
    return render(request, 'accounts/base.html')
def base1(request):
    return render(request, 'accounts/base1.html')
def base3(request):
    return render(request, 'accounts/base3.html')
def base4(request):
    return render(request, 'accounts/base4.html')
def base5(request):
    return render(request, 'accounts/base5.html')
def base6(request):
    return render(request, 'accounts/base6.html')
def schedule(request):
    return render(request, 'accounts/schedule.html')