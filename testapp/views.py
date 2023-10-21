from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def home(request):
    return render(request,'index.html')

def registration(request):
    error=""
    if request.method == "POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        em=request.POST['email']
        ec=request.POST['empcode']
        pwd=request.POST['pwd']

        try:
            user=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            EmployeeDetail.objects.create(user=user,empcode=ec)
            EmployeeExperince.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)

            error="no"
        except:
            error="yes"

    my_dict = {
          "error" :error,
        }

    return render(request,'registration.html',context=my_dict)


def emp_login(request):
    error= ""
    if request.method == 'POST':
        u = request.POST['emailid2']
        p = request.POST['password1']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    return render(request,'login.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'emp_home.html',locals())


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    error=""
    if request.method == "POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        em=request.POST['empcode']
        dept=request.POST['department']
        desi=request.POST['designation']
        contact=request.POST['contact']
        jdate=request.POST['jdate']
        gender=request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = em
        employee.empdept = dept
        employee.designation = desi
        employee.contact = contact
        employee.gender = gender


        if jdate:
            employee.joiningdate = jdate



        try:
            employee.save()
            employee.user.save()
            error="no"
        except:
            error="yes"


    my_dict = {
          "error" :error,
          "employee": employee,
        }

    return render(request,'profile.html',context=my_dict)

def Logout(request):
    logout(request)
    return redirect('home')

def admin_login(request):
    return render(request,'admin_login.html')

def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    experience = EmployeeExperince.objects.get(user=user)


    return render(request,'myexperience.html',locals())

def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    experience = EmployeeExperince.objects.get(user=user)
    error=""
    if request.method == "POST":
        company1name=request.POST['company1name']
        company1desig=request.POST['company1desig']
        company1sal=request.POST['company1sal']
        company1duration=request.POST['company1duration']
        company2name=request.POST['company2name']
        company2desig=request.POST['company2desig']
        company2sal=request.POST['company2sal']
        company2duration=request.POST['company2duration']
        company3name=request.POST['company3name']
        company3desig=request.POST['company3desig']
        company3sal=request.POST['company3sal']
        company3duration=request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1sal=company1sal
        experience.ecompany1duration = company1duration
        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2sal=company2sal
        experience.ecompany2duration = company2duration
        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3sal=company3sal
        experience.ecompany3duration = company3duration

        try:
            experience.save()
            error="no"
        except:
            error="yes"


    return render(request,'edit_experience.html',locals())

def my_education(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    education = EmployeeEducation.objects.get(user=user)


    return render(request,'my_education.html',locals())

def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    error=""
    if request.method == "POST":
        coursepg=request.POST['coursepg']
        schoolclgpg=request.POST['schoolclgpg']
        yearofpassingpg=request.POST['yearofpassingpg']
        percentagepg=request.POST['percentagepg']
        courseug=request.POST['courseug']
        schoolclgug=request.POST['schoolclgug']
        yearofpassingug=request.POST['yearofpassingug']
        percentageug=request.POST['percentageug']
        coursessc=request.POST['coursessc']
        yearofpassingssc=request.POST['yearofpassingssc']
        percentagessc=request.POST['percentagessc']
        schoolclgssc=request.POST['schoolclgssc']
        coursehsc=request.POST['coursehsc']
        yearofpassinghsc=request.POST['yearofpassinghsc']
        percentagehsc=request.POST['percentagehsc']
        schoolclghsc=request.POST['schoolclghsc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg=yearofpassingpg
        education.percentagepg = percentagepg
        education.courseug = courseug
        education.schoolclgug = schoolclgug
        education.yearofpassingug=yearofpassingug
        education.percentageug = percentageug
        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc=yearofpassingssc
        education.percentagessc = percentagessc
        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc=yearofpassinghsc
        education.percentagehsc = percentagehsc



        try:
            education.save()
            error="no"
        except:
            error="yes"


    return render(request,'edit_myeducation.html',locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    error = ""

    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"

    return render(request,'change_password.html',locals())

def admin_login(request):
    error= ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
        except:
            error = "yes"
    return render(request,'admin_login.html',locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = request.user
    error = ""

    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"

    return render(request,'change_passwordadmin.html',locals())

def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeDetail.objects.all()

    return render(request,'all_employee.html',locals())


def edit_education(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=pid)
    education = EmployeeEducation.objects.get(user=user)
    error=""
    if request.method == "POST":
        coursepg=request.POST['coursepg']
        schoolclgpg=request.POST['schoolclgpg']
        yearofpassingpg=request.POST['yearofpassingpg']
        percentagepg=request.POST['percentagepg']
        courseug=request.POST['courseug']
        schoolclgug=request.POST['schoolclgug']
        yearofpassingug=request.POST['yearofpassingug']
        percentageug=request.POST['percentageug']
        coursessc=request.POST['coursessc']
        yearofpassingssc=request.POST['yearofpassingssc']
        percentagessc=request.POST['percentagessc']
        schoolclgssc=request.POST['schoolclgssc']
        coursehsc=request.POST['coursehsc']
        yearofpassinghsc=request.POST['yearofpassinghsc']
        percentagehsc=request.POST['percentagehsc']
        schoolclghsc=request.POST['schoolclghsc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg=yearofpassingpg
        education.percentagepg = percentagepg
        education.courseug = courseug
        education.schoolclgug = schoolclgug
        education.yearofpassingug=yearofpassingug
        education.percentageug = percentageug
        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc=yearofpassingssc
        education.percentagessc = percentagessc
        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc=yearofpassinghsc
        education.percentagehsc = percentagehsc



        try:
            education.save()
            error="no"
        except:
            error="yes"


    return render(request,'edit_education.html',locals())


def delete_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=pid)
    #education = EmployeeEducation.objects.get(user=user)
    try:
        User.objects.filter(username=user).delete()
        return redirect('/all_employee')
    except:
        return render(request,'all_employee.html',locals())


    return render(request,'all_employee.html',locals())
