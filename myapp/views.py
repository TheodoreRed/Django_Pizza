from django.shortcuts import render, redirect
from .forms import PizzaForm
from .models import Pizza
from datetime import datetime

# Create your views here.
def hello(request):
    msg = "Hello There!"

    return render(request, "hello.html", {"hello_message": msg})


def index(request):
    pizza_posts = Pizza.objects.all().order_by("-published_date")
    return render(request, "index.html", {"pizza_posts": pizza_posts})


def new_post(request):
    return render(request, "new-post.html")


def info(request):
    return render(request, "info.html")


def new_post(request):
    form = PizzaForm(request.POST)
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "new-post.html", {"form": form})
