from django.shortcuts import render,redirect
from .models import Test,Employee, DesingnationTypes
from .forms import EmployeeForm 
# Create your views here.
def create(request):
    rolesList = DesingnationTypes.objects.all().values()
    if request.method=="POST":
        # name = form.cleaned_data['name']
        # active_field = form.cleaned_data['active_field']
        # address = form.cleaned_data['address']
        # city = form.cleaned_data['city']
        # country = form.cleaned_data['country']
        # zipcode = form.cleaned_data['zipcode']
        # state = form.cleaned_data['state']
        # designation = form.cleaned_data['designation']
        # name = form.cleaned_data['name']
        # name = form.cleaned_data['name']
        form = EmployeeForm(request.POST)
        checkbox = (request.POST.get('active_field','')=='on')
        if form.is_valid():    
            e = Test.objects.create(name=request.POST['name'],address=request.POST['address'],city=request.POST['city'],country=request.POST['country'],zipcode=request.POST['zipcode'],state=request.POST['state'],designation=request.POST['designation'],date_of_birth=request.POST['date_of_birth'],date_of_joining=request.POST['date_of_joining'],active_field=checkbox)
            return redirect('employeelist')
    else:
        form=EmployeeForm()     
    return render(request,'create.html',{'activePage' : "Create",'form':form,'rolesList':rolesList})
def edit(request,id):
    getEmp = Test.objects.filter(empId=id).values()[0] 
    return render(request,'edit.html',{'activePage' : "Edit",'data':getEmp})

def employee(request):
    e = Test.objects.all() # get all the employees in Db as objects
    elist = e.values()
    condition = len(elist)>0
    print(condition)
    # elist=1
    return render(request,'employee.html',{'activePage' : "Employee", 'EmployeeData': elist,'NoEmpview':condition})
def home(request):
    return render(request,'home.html',{'activePage' : "Home"})