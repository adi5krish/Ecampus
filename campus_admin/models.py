from django.db import models
from django.contrib.auth.models import User


class Semester(models.Model):
    semesterNo = models.IntegerField(default='',primary_key=True)

    def __str__(self):
        return str(self.semesterNo)


class Faculty(models.Model):

    facultyId = models.IntegerField(default=0,primary_key=True)
    facultyName = models.CharField(default='',max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.facultyName)


class Courses(models.Model):
    courseNo = models.CharField(max_length = 10, default = '',primary_key = True)
    courseName = models.CharField(max_length = 100, default = '',null=True,blank=True)
    credits = models.IntegerField(default = 0,null=True,blank=True)
    offered_In = models.ForeignKey(Semester, null=True, blank=True)
    elective = models.NullBooleanField()
    BRANCH = (
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('CS&IT', 'Computer Science and Information Technology')
    )
    offered_to = models.CharField(max_length=20, null=True, choices=BRANCH)
    assigned_to = models.ForeignKey(Faculty,null=True,blank=True)

    def __str__(self):
        return self.courseNo


class Student(models.Model):
    studentId = models.IntegerField(default=0, primary_key=True)
    studentName = models.CharField(max_length=100, default='')
    batch = models.CharField(default = '',max_length=20)
    programName = models.CharField(max_length=20,default='',null=True)

    def __str__(self):
        return self.studentName


class Registers(models.Model):
    studentId = models.ForeignKey(Student,related_name='%(class)s_studentId',null=True)
    semesterNo = models.ForeignKey(Semester, related_name='semesterNo+', null=True)
    courseNo = models.ForeignKey(Courses, related_name='courseNo+', null=True)
    grade = models.CharField(max_length=4,null=True,blank=True)

    class Meta:
        unique_together = (('semesterNo','courseNo','studentId'),)


class FeeReceipt(models.Model):
    studentId = models.ForeignKey(Student,related_name='%(class)s_studentId',null=False,default="0")
    semesterNo = models.ForeignKey(Semester, related_name='semesterNo+', null=True)
    receiptId = models.CharField(max_length=30,null=False,blank=True,default="0")
    status = models.CharField(max_length=50,null=False,blank=True,default='Not Paid')

    class Meta:
        unique_together = (('semesterNo','studentId'),)


class Result(models.Model):
    studentId = models.ForeignKey(Student, related_name='studentId+')
    semesterNo = models.ForeignKey(Semester, null=True, related_name='semesterNo+')
    SPI = models.FloatField(default='',blank=True,null=True)

    class Meta:
        unique_together = (('semesterNo','studentId'),)