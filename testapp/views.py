from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable' : 20,
        'name' : 'santhosh',
    }
    return render(request,'index.html',context)
    # return HttpResponse('Hello world')

def about(request):
    return HttpResponse('About page')

def services(request):
    return HttpResponse('Services page')