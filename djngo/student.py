class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")
    def __str__(self):
        return self.course_name

class Batch:
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")
    def __str__(self):
        return self.batch_code

class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.email=kwargs.get("email")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.student_name

django=Course()
django.add_course(course_name="django",status=True)
mein_stack=Course()
mein_stack.add_course(course_name="mein_stack",status=True)

djb1=Batch()
djb1.add_batch(course=django,batch_code="djmay2k22b1",start_date="12-6-2022")
mnb1=Batch()
mnb1.add_batch(course=mein_stack,batch_code="mnmay2k22b1",start_date="12-6-2022")

vishnu=Student()
vishnu.add_student(student_name="vishnu",email="vishnu@gamil",batch=djb1) #course is django
ravi=Student()
ravi.add_student(student_name="ravi",email="ravi@gamil",batch=djb1)
ajith=Student()
ajith.add_student(student_name="ajith",email="aji@gamil",batch=mnb1) #course is mein stack
rahul=Student()
rahul.add_student(student_name="rahul",email="rahul@gamil",batch=mnb1)

student=[]
student.append(vishnu)
student.append(ravi)
student.append(ajith)
student.append(rahul)
for i in student:
    if (i.batch.course.course_name=="mein_stack"):
        print(i)
        #or
ms_stud=[i.student_name for i in student if i.batch.course.course_name=="mein_stack"]
print(ms_stud)

print(ajith.batch)
# print(vishnu)

# print(djb1)
# print(djb1.course)
# print(djb1.course.status)