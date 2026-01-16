from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.models import Profile

from .forms import LoginForm, RegisterForm

# Create your views here.


def register_view(request):
    if request.method == "GET":
        forms_obj = RegisterForm()
        return render(request, "users/register.html", context={"form": forms_obj})
    elif request.method == "POST":
        forms_obj = RegisterForm(request.POST, request.FILES)
        if forms_obj.is_valid():
            forms_obj.cleaned_data.__delitem__("confirm_password")
            age = forms_obj.cleaned_data.pop("age")
            photo = forms_obj.cleaned_data.pop("photo")
            user = User.objects.create_user(**forms_obj.cleaned_data)
            if user:
                Profile.objects.create(user=user, age=age, photo=photo)
            return redirect("/login/")
        return HttpResponse("Invalid form")


def login_view(request):
    if request.method == "GET":
        forms_obj = LoginForm()
        return render(request, "users/login.html", context={"form": forms_obj})
    elif request.method == "POST":
        forms_obj = LoginForm(request.POST)
        if forms_obj.is_valid():
            user = authenticate(**forms_obj.cleaned_data)
            if user:
                login(request, user)
            return redirect("/")


@login_required(login_url="/login/")
def logout_view(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")


@login_required(login_url="/login/")
def profile_view(request):
    if request.method == "GET":
        user = request.user
        products = user.product.all()
        return render(
            request, "users/profile.html", context={"user": user, "products": products}
        )
