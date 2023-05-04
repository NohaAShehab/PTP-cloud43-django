from django.shortcuts import render, redirect , reverse
from  django.http import HttpResponse
# Create your views here.
from  students.models import Student


def helloworld(request):
    print("---- request received----")
    return HttpResponse("Hello world")


students=  ['Ahmed', 'Mohamed', 'Gehad']
def allstudents(request):
    return HttpResponse(students)


def getstudent(request, id):
    # return HttpResponse(id)
    if id in range(len(students)):
        return HttpResponse(students[id])
    else:
        return HttpResponse("<h1> Student not found </h1>")


def landingpage(request):
    return render(request, 'landing.html')



def studnets_list(request):
    return render(request,'list.html',context={"allstudents": students}  )


def students_index(request):
    # students= Student.objects.all()
    students = Student.get_all_students()
    return render(request, 'students/index.html', context={"students":students})

def student_delete(request, id):
    # students= Student.objects.all()
    student = Student.get_student(id)
    student.delete()
    redirect_url = reverse('students.index')
    return redirect(redirect_url)
    # return HttpResponse("object deleted")


def student_show(request, id):
    # students= Student.objects.all()
    student = Student.get_student(id)
    return render(request, 'students/show.html', context={"student":student})


from students.forms import  StudentForm
def create_student(request):
    form  = StudentForm()
    if request.method =='GET':
        return render(request, 'students/create.html', context={"form":form})
    else:
        print(request.POST)
        ## upload image 000> request.FILES
        print(request.FILES)
        ## use form object to save data
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        # return HttpResponse("POST request received")
        redirect_url = reverse('students.index')
        return redirect(redirect_url)

def edit_student(request, id ):
    student = Student.get_student(id)
    if request.method =='GET':
        form = StudentForm(instance=student)
        return render(request, 'students/edit.html', context={"form":form})
    else:
        print(request.POST)
        ## upload image 000> request.FILES
        print(request.FILES)
        ## use form object to save data
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
        # return HttpResponse("POST request received")
        redirect_url = reverse('students.show',args=[student.id])
        return redirect(redirect_url)
