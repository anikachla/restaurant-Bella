from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')  
    # path to reach index.html
    
    
def about(request):
    #return HttpResponse("My about page")
    return render(request,'about.html')

def contact(request):
    #return HttpResponse("My contact page")
    return render(request,'contact.html')

def menu(request):
    return render(request,'menu.html')

