from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'orm_practice/index.html', context)

def detail(request, pk):
    student = Student.objects.get(pk=pk)
    context = {
        'student': student,
    }
    return render(request, 'orm_practice/detail.html', context)

# create
def new(request):
    return render(request, 'orm_practice/new.html')

def create(request):
    student = Student()
    student.name = request.GET.get('name')
    student.age = request.GET.get('age')
    student.major = request.GET.get('major')
    student.hobby = request.GET.get('hobby')
    student.save()
    return redirect('detail', pk=student.pk)

