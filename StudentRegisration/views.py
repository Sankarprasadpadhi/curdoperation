from django.shortcuts import render, redirect
from StudentRegisration.models import StudentData


def home(request):
    return render(request, 'home.html')


def show(request):
    sdata = StudentData.objects.all()
    data = {
        'data': sdata
    }
    return render(request, 'show.html', data)


def add_student(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        address = request.POST["address"]
        StudentData(
            first_name=first_name, last_name=last_name, email=email, mobile=mobile, address=address
        ).save()
        return redirect('show')
    return render(request, 'add_student.html')


def edit_student(request, id):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        address = request.POST["address"]
        StudentData.objects.filter(id = id).update(
            first_name=first_name, last_name=last_name, email=email, mobile=mobile, address=address
        )
        return redirect('show')
    sdata = StudentData.objects.get(id=id)
    data = {
        'id': id,
        'data': sdata
    }
    return render(request, 'edit.html', data)


def delete_student(request, id):
    StudentData.objects.get(id=id).delete()
    return redirect('show')