from django.contrib import admin
from django.shortcuts import render,redirect
from Teacher.models import Faculty
from Student.models import Student_data,announcement,Attendance,Course,enquiry
import pandas as pd  

# Create your views here.
def login_Teacher(request):
	if request.method=="POST":
		mail= request.POST['full-name']
		password=request.POST['password']

		data=Faculty.objects.all()

		for i in data:
			if mail==i.Email:
				if password=="Svvv@123":
					key=i.FacultyID

					return Teacher_profile(request,key)
				else:
					msg="Incorrect Password"
					return render(request,"Login_Teacher.html",{"Msg":msg})

		msg="User Not Found"
		return render(request,"Login_Teacher.html",{"Msg":msg})

	msg=""
	return render(request,"Login_Teacher.html",{"Msg":msg})

def Teacher_profile(request,key):
	data=Faculty.objects.get(FacultyID=key)
	Username=data.Name
	return render(request,"Teacher_profile.html",{"Username":Username,"KEY":key})

def Teacher_info(request,key):
	data=Faculty.objects.get(pk=key)
	uname=data.Name
	return render(request,"Teacher_info.html",{"data":data,"Username":uname})

'''
def Teacher_Attendence(request,key):
	data=Faculty.objects.get(pk=key)
	uname=data.Name
	stud=Student_data.objects.filter(year=4)
	corse=Course.objects.all()

	return render(request,"Teacher_attendence.html",{"data":data,"Username":uname,"stud":stud,"corse":corse})
'''
def Teacher_Grading(request,key):
	data=Faculty.objects.get(pk=key)
	uname=data.Name
	stud=Student_data.objects.filter(year=4)
	corse=Course.objects.all()
	return render(request,"Teacher_grading.html",{"data":data,"Username":uname,"stud":stud,"corse":corse})

def Teacher_Annoncement(request,key):
	data=Faculty.objects.get(pk=key)
	uname=data.Name
	if request.method=="POST":
		title=request.POST['title']
		content=request.POST['content']
		entry= announcement(sender=data.Email,title=title,content=content)
		entry.save()
		allmsg=announcement.objects.all().reverse()

		print("data saved")
		return redirect('Teacher_Annoncement', key=key)
	
	allmsg=announcement.objects.all().reverse()
	return render(request,"Teacher_Annoncement.html",{"data":data,"Username":uname,"KEY":key,"msg":allmsg})



#from django.shortcuts import render
from django.http import HttpResponse
#from .models import Attendance, Student_data, Faculty, Course
from django.shortcuts import get_object_or_404

def Teacher_Attendence(request, key):
    data = get_object_or_404(Faculty, pk=key)
    uname = data.Name
    stud = Student_data.objects.filter(year=4)
    corse = Course.objects.all()

    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        teacher_name = uname
        selected_students = request.POST.getlist('student_id')  # Retrieve selected student IDs

        course = get_object_or_404(Course, pk=course_id)

        for student_id in selected_students:
            student = get_object_or_404(Student_data, pk=student_id)
            attendance = Attendance(student_id=student, course=course, present=True, teacher_name=teacher_name)
            attendance.save()
 
            # Creating Attendance objects for selected students

        return HttpResponse("<h1> Attendance saved successfully! </h1>")
    else:
        return render(request, "Teacher_attendence.html", {"data": data, "Username": uname, "stud": stud, "corse": corse})
