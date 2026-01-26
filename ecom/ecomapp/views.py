from django.shortcuts import render, redirect
from .models import Product, Student
from .forms import StudentForm
import requests
from django.http import JsonResponse
# Create your views here.

def home(request):
   
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})



from django.shortcuts import render, redirect


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'student_detail.html', {'student': student})



def call_rest_api(request):
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url, verify=False)

    # Convert response to Python dict
    data = response.json()

    return JsonResponse(data)
