from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method != "POST":
        return redirect('/')
    request.session['name'] = request.POST['name']
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    return redirect(f'/results')
    
def results(request):
    # context = {
    #     'name': request.session['name'],
    #     'language': request.session['language'],
    #     'location': request.session['location']
    # }
    return render(request, 'results.html')






