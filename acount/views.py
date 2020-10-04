# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from . import forms
#
#
# # Create your views here.
# class SignUP(CreateView):
#     form_class = forms.UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/register.html'

# from .forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic
# from django.contrib.auth import authenticate, login
# from .forms import UserCreationForm
#
#
# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/register.html'


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy

from acount.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            account = authenticate(email=email, password=raw_password)
            login(request, account)
            success_url = reverse_lazy('login')




        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/home')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('/home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)


    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    # print(form)
    return render(request, "accounts/login.html", context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(

            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

    context['account_form'] = form

    return render(request, "accounts/account.html", context)


def must_authenticate_view(request):
    return render(request, 'accounts/must_authenticate.html')
