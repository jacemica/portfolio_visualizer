from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse("<h1>Home</h1>")

def test(request):
    return render(request, 'home/test.html') 