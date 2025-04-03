from django.shortcuts import render, redirect

def main(request):
    return render(request,'main.html')

def about(request):
    return render(request,'about.html')

def contacts(request):
    return render(request,'contacts.html')
