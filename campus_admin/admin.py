from django.contrib import admin
from .models import (

    Student,
    Semester,
    Courses,
    Result,
    Registers,
    FeeReceipt,
    Faculty,

)

admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Courses)
admin.site.register(Result)
admin.site.register(Registers)
admin.site.register(FeeReceipt)
admin.site.register(Faculty)

