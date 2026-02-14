from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Course
from django.db.models import Q

# Create your views here.
# def welcome(request):
#     return HttpResponse('<h1> Finally Welcome to the Dashboard </h>')
# def v1(request):
#     x = 28
#     a = (f"<h2> The Value of x is : {x} </h2>")
#     return HttpResponse (a)
# def Name(request,user):
#     return HttpResponse (f"<h3> My Name is : {user} </h3>")
# def delete(request,x1,x2):
#     return HttpResponse(f"<h2> Deletion ID is {x1} and {x2}")
# def add(request):
#     x = 10
#     y = 20
#     z = x + y
#     return HttpResponse(f"Addition of x & y is : {z}")
# def form(request):
#     a = '''
#   <html>
#       <head> 
#         <title>My Form</title>
#       </head>
#       <body>
#         <form method="POST">
#           <table>
#             <tr>
#               <td>Heading</td>
#               <td><input type="text" name="bhead" /></td>
#             </tr>
#             <tr>
#               <td>Category</td>
#               <td><input type="text" name="bcat" /></td>
#             </tr>
#             <tr>
#               <td colspan="2">
#                 <input type="submit" value="Submit" />
#               </td>
#             </tr>
#           </table>
#         </form>
#       </body>
#     </html>

#     '''
#     return HttpResponse(a)
# def html(request):
#     return render(request, "index.html")
# def index(request):
#     context = {}
#     context['Name'] = "Sudheer Muthyala"
#     context['Pin_No'] = 28
#     context['Mob_Num'] = 8688162274
#     context['email'] = "sudheermuthyala5@gmail.com"
#     return render (request, 'index.html', context)

# def index(request):
#     context = {}
#     context['x'] = 300
#     context['y'] = 200
#     return render(request, 'index.html', context)

# def index(request):
#     content = {}
#     content['a'] = [10, 20, "Sudheer", True, 98.56]
#     return render(request, 'index.html', content)

# def index(request):
#     content = {}
#     content['dict'] = {'FirstName':"Sudheer", 'SureName':"Muthyala", 'Mobile Number': 8688162274, 'Email':"sudheermuthyala5@gmail.com", 'Pin No': "22T91A0428", 'College Name': "Giet Engineering College"}
#     return render(request, 'index.html', content)

# def contact(request):
#     return render(request, 'contact.html')
# def placement(request):
#     return render(request, 'placement.html')

# def create(request):
#     return render(request, "index.html")
# def store(request):
#     h = request.POST['bhead']
#     c = request.POST['bcat']
#     d = request.POST['bdesc']
#     Data = h + " " + c + " " + d
#     return HttpResponse(Data)

import datetime
def date_time(request):
    cont = {}
    now = datetime.datetime.now()
    cont["d_t"] = now
    return render(request, "date_time.html", cont)

def hello(request):
    return render(request, "hello.html")

# After Connecting to the sqlite
def course(request):
    return render(request, "create_course.html")

def create_course(request):
    if request.method == "POST":
        x = request.POST['cname']
        y = request.POST['cdur']
        z = request.POST['cprice']
        c1 = Course.objects.create(cname = x, cdur = y, cprice = z)
        c1.save()
    return redirect('/')

def get_course(request):
    cont = {}
    cont['data'] = Course.objects.all()
    return render(request, 'dashboard.html', cont)

def delete(request,rid):
    x = Course.objects.get(id = rid)
    x.delete()
    return redirect('/')

def edit(request,rid):
    # Getting the Data from Database Based on id
    if request.method == "POST":
        x = request.POST['cname']
        y = request.POST['cdur']
        z = request.POST['cprice']
        c = Course.objects.filter(id = rid)
        # After the fetching it Have to Update 
        c.update(cname = x, cdur = y, cprice = z)
        # After it have to be Redirected
        return redirect('/')
    else:
        cont = {}
        cont['data'] = Course.objects.get(id = rid)
        return render(request, 'edit_course.html', cont)
    
# Suppose if i Want to Find the Course Which Has around 60 days Duration 
# Filtering the Records Which is 60 as cdur  
def filter_records(request):
    cont = {}
    cont['data'] = Course.objects.filter(cdur = 60)
    return render(request, 'dashboard.html', cont)

# If We Want the cprice is Less_than(__lt) 40000
# If We Want Greater Than(__gt) > 40000

# Filter & order_by
def filter_records(request):
    cont = {}
    q1 = Q(cdur__lt = 60)
    q2 = Q(cprice__gt = 45000)
    cont['data'] = Course.objects.order_by("cdur").filter(cprice__gt = 40000)
    return render(request, 'dashboard.html', cont) 

# When i Enter the Data in the Form , Data Has to be Show in the Terminal as well as Database Student
from . form import student_registration
from . models import student

def showform(request):
    if request.method == "POST":
        fn = student_registration(request.POST)
        if fn.is_valid():
            sname = fn.cleaned_data['name']
            semail = fn.cleaned_data['email']
            s1 = student.objects.create(name = sname, email = semail)
            s1.save()
        else:
            print("Data is Not Valid")
    else:
        fn = student_registration()
        print(fn)
    return render (request, 'dform.html', {'form':fn})

# from . models import fn
from django.contrib.auth.forms import UserCreationForm
# We Haven't Gave anyithing in the models to Save Password and User Name I used "User"
from django.contrib.auth.models import User
# from . form import Signupform

# Signup Form That Stores Username && Password in the Database (Auth_user)
def register(request):
    if request.method == "POST":
        fn = UserCreationForm(request.POST)
        if fn.is_valid():
            uname = fn.cleaned_data['username']
            upass = fn.cleaned_data['password1']
            # Create_user Comverts Raw Password into Hashcode in the Database
            u1 = User.objects.create_user(username = uname, password = upass)
            u1.save()
            print(uname)
            print(upass)
    else:
        fn = UserCreationForm()
    return render(request,'signup.html',{'form':fn})


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password'] 
            user = authenticate(username = uname, password = upass)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form':form})

def user_profile(request):
    return render (request, 'profile.html')

def user_logout(request):
    logout(request)
    return redirect("login")

def set_cookie(request):
    res = render (request,'setcookie.html')
    res.set_cookie('name','Project.com')
    return res

def get_cookie(request):
    value = request.COOKIES.get('name','Guest')
    return render(request, 'getcookie.html', {'value': value})

def del_cookie(request):
    val = render(request, 'delcookie.html')
    val.delete_cookie('name')
    return val

def set_session(request):
    request.session['name'] = 'Project1.com'
    return render(request, 'setsession.html')

def get_session(request):
    nam = request.session.get('name','Guest')
    return render(request, 'getsession.html', {'value': nam})

def del_session(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'delsession.html')