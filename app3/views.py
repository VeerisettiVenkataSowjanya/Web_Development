from django.shortcuts import render
from django.http import HttpResponse
from app3.forms import StudentForm

# Create your views here.
def demo(request):
	return HttpResponse('I am from app3')

def reg(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		form.save()
		return HttpResponse('Data Inserted using forms')

	form = StudentForm()
	return render(request,'FormsApp/reg.html',{'form':form})