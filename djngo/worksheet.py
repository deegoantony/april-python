#class=course_name,status,return:course_name
#batch=course,batchcode,startdate return:batch code
#student=student name,email,batch

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
        self.startdate=kwargs.get("start_date")

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
mearnstack=Course()
mearnstack.add_course(course_name="mearnstack",status=True)

djb1=Batch()
djb1.add_batch(course=django,batch_code="djmay2k22",stardate="12-6-2022")
mnb1=Batch()
mnb1.add_batch(course=mearnstack,batch_code="mnmay2k22",stardate="12-6-2022")
vishnu=Student()
vishnu.add_student(student_name="vishnu",email="vishnu@gamil",batch=djb1)
anu=Student()
anu.add_student(student_name="anu",email="anu@gamil",batch=mnb1)
print(vishnu.batch.course)

