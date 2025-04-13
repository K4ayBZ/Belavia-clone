from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Авторизуем пользователя после регистрации
            return redirect('flights:search_flights')  # Перенаправляем на страницу поиска рейсов
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'accounts/templates/registration/login.html'