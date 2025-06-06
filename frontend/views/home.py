from django.shortcuts import render


def home(request):
    return render(request, "base.html")


def brands_list(request):
    return render(request, "brands/brands_list.html")