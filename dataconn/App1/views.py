from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymysql import *
con=Connect(host='127.0.0.1',user='root', password='root',database='shiva')
cr=con.cursor()
def home(request):
   return render(request, 'signup.html')

@csrf_exempt
def sign(request):
    name = request.POST.get('uname')
    password = request.POST.get('password')
    s= "select * from detail"
    cr.execute(s)
    l=cr.fetchall()
    for i in l:
       if i[0]== name:
          return HttpResponse("Username already existed")
    s="insert into detail values('{}','{}')".format(name,password)
    cr.execute(s)
    con.commit()
    return HttpResponse("Data inserted sucesfully")
def login(request):
   return render(request,'login.html')
@csrf_exempt
def logi(request):
    name=request.POST.get('uname')
    password=request.POST.get('password')
    s="select * from detail"
    cr.execute(s)
    l=cr.fetchall()
    for i in l:
        if i[0]==name and i[1]==password:
            return HttpResponse("Login Successful")
    else:
        return HttpResponse('Invalid Login Credentials')

def forget(request):
   return render(request,'forget.html')
@csrf_exempt

def Forgot(request):
   name = request.POST.get('uname')
   s = "select * from detail"
   cr.execute(s)
   l=cr.fetchall()
   for i in l:
      if i[0]==name:
         return HttpResponse(i[1])
   else:
         return HttpResponse('Invalid username')

def change(request):
   return render(request,'change.html')
@csrf_exempt
def chng(request):
   name = request.POST.get('uname')
   password = request.POST.get('password')
   cpass = request.POST.get('cpassword')
   s = "select * from detail"
   cr.execute(s)
   l=cr.fetchall()
   for i in l:
      if i[0]==name and i[1]==password:
         s1 = "update detail set pass='{}' where name='{}'".format(cpass,name)
         cr.execute(s1)
         con.commit()
         return HttpResponse('Successfully changed')
   else:
         return HttpResponse('Invalid username')