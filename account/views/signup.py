from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import SignupForm
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'pages/signup.html', context={'form': form})
