from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
# Create your views here.
# create
# html 제공
def new(request):
    return render(request, 'orm_practice/new.html')
# 실제 저장
def create(request):
    if request.method == 'POST':
        student = Student()
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.major = request.POST.get('major')
        student.hobby = request.POST.get('hobby')
        student.save()
        return redirect('detail', pk=student.pk)
    else:
        return redirect('new')

# Read  
def index(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'orm_practice/index.html', context)

def detail(request, pk):
    # student = Student.objects.get(pk=pk)
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student,
    }
    return render(request, 'orm_practice/detail.html', context)



# Update
## 수정용 html 제공
def edit(request, pk):
    student = Student.objects.get(pk=pk) # 수정하고자 하는 객체 잡기 
    context = {
        'student': student
    }
    return render(request, 'orm_practice/edit.html', context)

## 실제 수정
def update(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk) # 수정하고자 하는 객체 잡기 
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.major = request.POST.get('major')
        student.hobby = request.POST.get('hobby')
        student.save()
        return redirect('detail', pk=student.pk)
    else:
        return redirect('edit', pk=pk)

# Delete
def delete(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk) # 수정하고자 하는 객체 잡기 
        student.delete()
        return redirect('index')
    else:
        return redirect('detail', pk=pk)