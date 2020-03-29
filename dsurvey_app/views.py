from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == "POST":
        context = {
            'name': request.POST['name'],
            'lang': request.POST['language'],
            'loca': request.POST['location']
        }
        return render(request, "result.html", context)
    return render(request, "result.html")
    







