from django.shortcuts import render

def info(request):
    return render(request, 'main/info.html')

def allergia(request):
    return render(request, 'main/allergia.html')



