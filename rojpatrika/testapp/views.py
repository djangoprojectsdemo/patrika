from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request ,'testapp/home.html')

def state_view(request):
    return render(request,'testapp/states.html')

def detail_view(request):
    return render(request,'testapp/detail.html')