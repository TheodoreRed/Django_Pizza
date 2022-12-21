from django.shortcuts import render

# Create your views here.
def hello(request):
    msg = "Hello There!"

    return render(request, "hello.html", {"hello_message": msg})


def index(request):
    return render(request, "index.html")


def new_post(request):
    return render(request, "new-post.html")


def info(request):
    return render(request, "info.html")
