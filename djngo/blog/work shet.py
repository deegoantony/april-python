from djngo.blog.models import users, posts


def authenticate(**kwargs):
    username = kwargs.get("username")
    email = kwargs.get("email")
    user_data = [users for u in users if u["username"] == username and u["email"] == email]
    return user_data

def login_function(fn):
    def inner_function(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            raise Exception("u must login first")
    return inner_function

session = {} #3


class SignInView:
    def post(self, *args, **kwargs):
        username = kwargs.get("username")
        email = kwargs.get("email")
        use = authenticate(username=username, email=email)
        if use:
            print("login success")
            session["user"] = username  # if log in success add user name in to a empty dictionary"session"
        else:
            print("invalid login")

@login_function
def logout(*args,**kwargs):
    session.pop("user")


class AllPostView:
    @login_function
    def get(self, *args, **kwargs):
        return posts

class MyPostView:
    @login_function
    def get(self,*args,**kwargs):
        username=session.get("user")
        userId=[i["id"] for i in users if i["username"]==username][0]
        post=[u for u in posts if u["userId"]==userId]
        print(post)


ob=SignInView()
ob.post(username="Bret",email="Sincere@april.biz")
od=MyPostView()
od.get()
