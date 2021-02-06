from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def sample1(request):
	return HttpResponse("<h1>welcome to django session</h1>")

def sample2(request):
	return HttpResponse("<center><h1>Good Morning</h1></center>")

def sample3(request):
	return HttpResponse("<p>hii hello good morning <br>welcome to the django session <br> we are learning web development using django</p>")

def sample4(request):
	return HttpResponse("<h1>WEB DEVELOPMENT</h1><br><h2>This is sowjanya</h2><br><p>We are learning web development using python and django platform</p><br><h5>organised by APSSDC at VITW</h5>")

def sample5(request,name,age):
	return HttpResponse("Hellooo....."+name+"<br>age : %d"%age)

def samplehtmlex(request):
	return render(request,'student/sample.html')

def internalcssex(request):
	return render(request,'student/demo.html')

def externalcssex(request):
	return render(request,'student/example.html')

def bootstrapex(request):
	return render(request,'student/bootstrap.html')

def login(request):
	return render(request,'student/loginpage.html')

def register(request):
	if request.method=='POST':
		Fname=request.POST.get('Firstname')
		Lname=request.POST.get('Lastname')
		Uname=request.POST.get('Username')
		Rollno=request.POST.get('Rollno')
		email=request.POST.get('email')
		pwd=request.POST.get('Password')
		cpwd=request.POST.get('CPassword')
		mobile=request.POST.get('Mobileno')
		#print(Fname,Lname,Uname)
		
		return render(request,'student/details.html',{'Fname':Fname,'Lname':Lname,'Uname':Uname,'Rollno':Rollno,'email':email,'pwd':pwd,'cpwd':cpwd,'mobile':mobile})
	return render(request,'student/register.html')