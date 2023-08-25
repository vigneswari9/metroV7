from django.shortcuts import render,redirect
from apps.forms import EmployeeForm

# Create your views here.
def emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            employee_instance=form.save()
            return redirect('success_page')
    else:
        form=EmployeeForm()
    return render(request,'index.html',{'form':form})
def success_view(request):
    return render(request,'success.html')