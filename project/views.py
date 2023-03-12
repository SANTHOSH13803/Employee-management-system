from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from datetime import date 
# Create your views here.\


# rolesList = DesingnationTypes.objects.all().values()
# rolesList = [i['role_name'] for i in (list(rolesList))]

def create(request):
    form = EmployeeForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.on_leave:
                instance.leave_count+=1
            instance.save()
            return redirect('employeelist')
    return render(request,'create.html',{'activePage' : "Create",'form':form})


def edit(request,id):
    employeeObj = Employee.objects.get(pk=id)
    # print(employeeObj.on_leave,employeeObj.leave_count)

    if(employeeObj.on_leave and employeeObj.leave_count==0):
        employeeObj.leave_count=1
        
    form = EmployeeForm(instance=employeeObj)
    if request.method =="POST":
        form =EmployeeForm(request.POST,instance = employeeObj) 
        if form.is_valid():
            instance = form.save(commit=False)
            # print(employeeObj.on_leave==False,'table')
            # print(request.POST.get('on_leave',''),'from form')
            # print(instance.on_leave==True and request.POST.get('on_leave','')==None ,'condition')
            if(instance.on_leave==True ):
                instance.leave_count+=1
            instance.save()
            return redirect('employeelist')
    return render(request,'edit.html',{'activePage' : "Edit",'data':employeeObj,'form' :form})


def employee(request):
    emplist = Employee.objects.all() # get all the employees in Db as objects
    condition = len(emplist)>0
    return render(request,'employee.html',{'activePage' : "Employee", 'EmployeeData': emplist,'NoEmpview':condition})
    
def home(request):
    employeeQuery = Employee.objects.all().values()
    onLeaveEmployees = [i['name'] for i in employeeQuery if i['on_leave']==True]
    activeEmployees = [i['name'] for i in employeeQuery if i['active_field']==True]
    length = len(employeeQuery)
    # print(onLeaveEmployees,activeEmployees,length)
    return render(request,'home.html',{'activePage' : "Home",'onleaveEmpls':onLeaveEmployees,'activeEmpls':activeEmployees,'empCount':length,'activeCondition':len(activeEmployees)==0,'onLeaveCondition':len(onLeaveEmployees)==0})

def employee_view(request,id):
    employeeObj = Employee.objects.get(pk=id)
    context = {'empData':employeeObj}
    return render(request,'employee_view.html',context)




# def edit_save(request,id):
#     #From DB
#     employeeObj = Test.objects.get(pk=id)

#     #from Edit HTML
#     if request.method =="POST":
#         name=request.POST.get('name')
#         address=request.POST.get('address')
#         city=request.POST.get('city')
#         country=request.POST.get('country')
#         zipcode=request.POST.get('zipcode')
#         state=request.POST.get('state')
#         designation=request.POST.get('designation')
#         date_of_birth=request.POST.get('date_of_birth')
#         date_of_joining=request.POST.get('date_of_joining')
#         active_field=request.POST.get('active_field','')=='on' 

#         #modifing data in db
#         employeeObj.name = name
#         employeeObj.address = address
#         employeeObj.city = city
#         employeeObj.country = country
#         employeeObj.zipcode = zipcode
#         employeeObj.state = state
#         employeeObj.designation = designation
#         employeeObj.date_of_birth= date_of_birth
#         employeeObj.date_of_joining= date_of_joining
#         employeeObj.active_field= active_field

#         employeeObj.save()
#         return redirect('employeelist')