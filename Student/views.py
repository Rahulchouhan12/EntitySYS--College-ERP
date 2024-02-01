from django.shortcuts import render, redirect
from django.contrib import admin
from Student.models import Student_data,chats,announcement,Course,Attendance,enquiry,hostel,marks
from Teacher.models import Faculty

# Create your views here.

admin.site.register(Student_data)
admin.site.register(chats)
admin.site.register(Faculty)
admin.site.register(announcement)
admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(enquiry)
admin.site.register(hostel)
admin.site.register(marks)


def Home(request):
	return render(request,"Index.html")
''
def login_student(request):
	if request.method=="POST":
		enrollment= request.POST['full-name']
		password=request.POST['password']

		data=Student_data.objects.all()

		for i in data:
			if enrollment==i.sid:
				if password=="Svvv@123":
					key=i.id

					return student_profile(request,key)
				else:
					msg="Incorrect Password"
					return render(request,"Login_student.html",{"Msg":msg})

		msg="User Not Found"
		return render(request,"Login_student.html",{"Msg":msg})

	msg=""
	return render(request,"Login_student.html",{"Msg":msg})

def student_profile(request,key):
	data=Student_data.objects.get(id=key)
	Username=data.sfname
	return render(request,"Student_profile.html",{"Username":Username,"KEY":key})

def student_info(request,key):
	data=Student_data.objects.get(pk=key)
	uname=data.sfname
	return render(request,"Student_info.html",{"data":data,"Username":uname})

def student_classmates(request,key):
	data=Student_data.objects.all()
	stud=Student_data.objects.get(id=key)
	uname=stud.sfname
	return render(request,"Student_classmates.html",{"data":data,"Username":uname,"myenroll":stud,"KEY":key})

def student_chats(request, key, rkey):
    mydata = Student_data.objects.get(id=key)
    second = Student_data.objects.get(id=rkey)
    
    data = chats.objects.filter(sender=mydata.sid, reciver=second.sid) | chats.objects.filter(sender=second.sid, reciver=mydata.sid)

    if request.method == "POST":
        msg = request.POST["msg"]
        entry = chats(sender=mydata.sid, reciver=second.sid, message=msg)
        entry.save()
        data = chats.objects.filter(sender=mydata.sid, reciver=second.sid) | chats.objects.filter(sender=second.sid, reciver=mydata.sid)
        return redirect('student_chats', key=key, rkey=rkey) 
    return render(request, "Student_chat.html", {"data": data, "mydata": mydata, "second": second, "KEY": key})


def delete_entry(request, key, rkey, msgid):
    mysid = Student_data.objects.get(id=key)
    entry = chats.objects.get(sender=mysid.sid, id=msgid)
    entry.delete()
    return redirect('student_chats', key=key, rkey=rkey)


def student_attendence(request,key):
	data=Student_data.objects.get(pk=key)
	uname=data.sfname
	Attend= Attendance.objects.filter(student_id=key);
	count=0
	for i in Attend:
		count=count+1;
		teacher=i.teacher_name
	teacher="ANKITA SINGH"
	return render(request,"Student_attendence.html",{"data":data,"Username":uname,"count":count,"teacher":teacher})

def student_marks(request,key):
	data=Student_data.objects.get(pk=key)
	uname=data.sfname
	return render(request,"Student_Marks.html",{"data":data,"Username":uname})

def student_course(request,key):
	data=Student_data.objects.get(pk=key)
	uname=data.sfname
	return render(request,"Student_course.html",{"data":data,"Username":uname})

def Student_learning(request,key):
	data=Student_data.objects.get(pk=key)
	uname=data.sfname
	return render(request,"Student_learning.html",{"data":data,"Username":uname})


def Student_examform(request,key):
	data=Student_data.objects.get(pk=key)
	uname=data.sfname
	cours=Course.objects.filter(semester=data.semester)
	return render(request,"Student_examform.html",{"data":data,"Username":uname,"cours":cours})

def ask_teacher(request,key):
	data=Faculty.objects.all()
	data2=Student_data.objects.get(pk=key)
	uname=data2.sfname
	notice=announcement.objects.all()

	return render(request,"ask_teacher.html",{"teachers":data,"Username":uname,"msg":notice})


def enqry(request):
	if request.method=="POST":
		nm=request.POST['name']
		em=request.POST['email']
		msg=request.POST['message']
		data=enquiry(name=nm,email=em,msg=msg)
		data.save()

	return render(request,"Index.html")
