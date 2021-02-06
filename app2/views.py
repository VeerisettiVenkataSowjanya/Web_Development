from django.shortcuts import render,redirect
from django.http import HttpResponse
from app2.models import Student

# Create your views here.
def demo(request):
	return HttpResponse('From app2....')

def home(request):
	return render(request,'CrudApp/home.html')

def addstudent(request):
	if request.method == 'POST':
		fn=request.POST.get('fname')
		ln=request.POST.get('lname')
		name=request.POST.get('name')
		rno=request.POST.get('rnum')
		email=request.POST.get('email')
		mno=request.POST.get('mobile')
		g=request.POST.get('gender')
		a=request.POST.get('age')
		Student.objects.create(fname=fn,lname=ln,name=name,rnum=rno,email=email,mobile=mno,gender=g,age=a)
		return redirect('details2')
	return render(request,'CrudApp/addstudent.html')

def details2(request):
	info=Student.objects.all()
	content={'info':info}
	return render(request,'CrudApp/details2.html',content)

def update(request,id):
	data=Student.objects.get(id=id)
	if request.method=='POST':
		data.fname=request.POST['fname']
		data.lname=request.POST['lname']
		data.name=request.POST['name']
		data.rnum=request.POST['rnum']
		data.email=request.POST['email']
		data.mobile=request.POST['mobile']
		data.gender=request.POST['gender']
		data.age=request.POST['age']
		data.save()
		return redirect('details2')
	return render(request,'CrudApp/update.html',{'data':data})


def delete(request,id):
	obj=Student.objects.get(id=id)
	if request.method== 'POST':
		obj.delete()
		return redirect('details2')
	return render(request,'CrudApp/delete.html',{'obj':obj})