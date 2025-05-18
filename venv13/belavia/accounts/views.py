from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

from .forms import UserRegistrationForm


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


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})
from django.contrib.auth.views import LoginView

def logout(request):
    return render(request, 'accounts/logout.html')


class CustomLoginView(LoginView):
    template_name = 'accounts/templates/accounts/login.html'