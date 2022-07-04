# user,course,batch
def admin_permision_requried(fn):
    def inner_function(*args, **kwargs):
        user = kwargs.get("user")
        if user.role != "admin":
            raise Exception("permission denied")
        else:
            return fn(*args, **kwargs)

    return inner_function


class User:
    def setuser(self, username, role):
        self.username = username
        self.role = role

    def print_data(self):
        print(self.username, self.role)


class Course:
    @admin_permision_requried
    def set_course(self, *args, **kwargs):
        self.user = kwargs.get("user")
        self.course_name = kwargs.get("course_name")

    def print_data(self):
        print(self.course_name)


class Batch:
    @admin_permision_requried
    def set_batch(self, *args, **kwargs):
        self.user = kwargs.get("user")
        self.batch_code = kwargs.get("b_code")
        self.course = kwargs.get("course")

    def print_data(self):
        print(self.batch_code)


user = User()
user.setuser("rahul", "admin")
course = Course()
course.set_course(user=user, course_name="django")
batch = Batch()
batch.set_batch(user=user, b_code="aprdjango", course=course)

course.print_data()
