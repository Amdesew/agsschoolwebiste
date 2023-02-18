from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Grade_Nine, Grade_Ten, Grade_Eleven, Grade_Twelve, New_Students

def home(request):
    return render(request, 'home.html')

def student_register(request):
    new_student = New_Students.objects.all()

    if request.method == "POST":
        f_name = request.POST['name']
        st_class = request.POST['wanted_class']
        st_phone = request.POST['phone_no']

        new_student = New_Students(
            full_name = f_name,
            phone_number = st_phone,
            wanted_class = st_class
        )

        new_student.save()
        return redirect('/thankyou')
    else:
        print("failed")
 
    return render(request, 'student_register.html')

def student_result(request):
    students = ''
    if 'q' in request.GET:
        q = request.GET['q']
        students = Grade_Nine.objects.filter(no=q) or Grade_Eleven.objects.filter(no=q) or  Grade_Ten.objects.filter(no=q) or Grade_Twelve.objects.filter(no=q)
    else:
        print("Failed")
    return render(request, 'student_result.html', {'students': students})

def notification(request):
    return render(request, 'notification.html')

def about_us(request):
    return render(request, 'about_us.html')

def back_door(request):
    return render(request, 'back_door.html')

def thankyou_page(request):
    return render(request, 'thankyou.html')