from django.db import models
import datetime
# Create your models here.
class Student_data(models.Model):
	sid=models.CharField(max_length=20,unique=True)
	sfname=models.TextField(max_length=30)
	gender=models.TextField(max_length=10)
	dob=models.DateField()
	address=models.TextField(max_length=50)
	mob=models.BigIntegerField()
	section=models.CharField(max_length=1,default="NA")
	degree=models.TextField(max_length=30,default="NA")
	branch=models.TextField(max_length=30,default="NA")
	year=models.IntegerField(default=1)
	semester=models.IntegerField(default=1)

class chats(models.Model):
	sender=models.CharField(max_length=20)
	reciver=models.CharField(max_length=20)
	message=models.TextField(max_length=300)
	time=models.DateTimeField(default=datetime.datetime.now())

class announcement(models.Model):
	sender=models.CharField(max_length=50)
	title=models.TextField(max_length=100)
	content=models.TextField(max_length=500)
	time=models.DateTimeField(default=datetime.datetime.now())

class Course(models.Model):
    SEMESTER_CHOICES = (
        (1, 'Semester 1'),
        (2, 'Semester 2'),
        (3, 'Semester 3'),
        (4, 'Semester 4'),
        (5, 'Semester 5'),
        (6, 'Semester 6'),
        (7, 'Semester 7'),
        (8, 'Semester 8'),
    )

    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    curriculum_link = models.CharField(max_length=200)

class Attendance(models.Model):
    student_id = models.ForeignKey(Student_data, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    present = models.BooleanField(default=False)  # Assuming True for present, False for absent
    teacher_name = models.CharField(max_length=50)  # Adding teacher's name field


class enquiry(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	msg=models.CharField(max_length=100)


class hostel(models.Model):
	name=models.CharField(max_length=20)
	seats=models.IntegerField()
	room=models.IntegerField()

class marks(models.Model):
	sid=models.CharField(max_length=30)
	ta=models.IntegerField()
	mst1=models.IntegerField()
	mst2=models.IntegerField()

'''
class Attendance(models.Model):
    student = models.CharField(max_length=30)
    course = models.CharField(max_length=50)
    present = models.BooleanField(default=False)  # Assuming True for present, False for absent
    teacher_name = models.CharField(max_length=50)  # Adding teacher's name field
'''