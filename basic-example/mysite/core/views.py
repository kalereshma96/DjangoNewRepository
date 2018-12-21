from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


@login_required
def home(request):
    """

        :param request:
        :return:  user request goes to home page
         after login or register.
        """
    return render(request, 'home.html')


def signup(request):
    """
        In this function user need to enter their
        information like username, password, email
        etc.
       :param request:
       :return:
       """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
