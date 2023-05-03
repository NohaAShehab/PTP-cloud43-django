from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.


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