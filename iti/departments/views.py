from django.shortcuts import render, redirect, reverse

# Create your views here.

from departments.models import  Department
def departments_index(request):
    departments =Department.get_all_departments()
    return render(request, 'departments/index.html',
                  context={"departments":departments})


def show_dept(request, dept_id):
    department = Department.get_specific_department(dept_id)
    return render(request, 'departments/show.html',
                  context={"department": department})


def delete_dept(request, dept_id):
    department = Department.get_specific_department(dept_id)
    department.delete()
    redirect_url = reverse('departments.index')
    return redirect(redirect_url)

