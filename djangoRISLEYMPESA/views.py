from django.shortcuts import render, redirect

def payuser(request):
    return render(request, "payments.html")