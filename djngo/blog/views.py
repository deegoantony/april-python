from djngo.blog.models import users, posts


# authenticate

# def authenticate(username,email):
#     user_data=[users for i in users if i["username"]==username and i["email"]==email]
#     return user_data
# user=authenticate("Bret","Sincere@april.biz")
#
# if user:
#     print("login success")
# else:
#     print("invalid credentials")


# or
def login_requried(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args, **kwargs)
        else:
            print("u must log in")

    return wrapper


@login_requried
def loged_user():
    username = session.get("user")
    userId = [user["id"] for user in users if user["username"] == username][0]
    return userId


def autthenticate(**kwargs):
    user_name = kwargs.get("username")  # .get used to remove the error genaration and show none
    email = kwargs.get("email")
    user_data = [users for i in users if i["username"] == user_name and i["email"] == email]
    return user_data


# user=autthenticate(username="Bret",email="Sincere@april.biz")
#
# if user:
#     print("login success")
# else:
#     print("invalid credentials")

# for singn in view:
session = {}  # for sign in user


class SignInView:
    def post(self, *args, **kwargs):
        username = kwargs.get("username")
        email = kwargs.get("email")
        user = autthenticate(username=username, email=email)
        if user:
            print("success")
            session["user"] = username
        else:
            print("invalid credential")


@login_requried
def logout(*args, **kwargs):  # for sing out
    session.pop("user")
    # if "user" in session:
    #     session.pop("user")
    #     print("user loged out")
    # else:
    #     print("u must log in")


class PostListView:
    @login_requried
    def get(self, *args, **kwargs):
        return posts


class MyPostView:
    @login_requried
    def get(self, *args, **kwargs):
        userId = loged_user()
        qs = [post for post in posts if post["userId"] == userId]
        return qs


class PostCreateView():
    @login_requried
    def post(self, *args, **kwargs):
        userId = loged_user()
        title = kwargs.get("title")
        body = kwargs.get("body")
        data = {
            "userId": userId,
            "title": title,
            "body": body
        }
        posts.append(data)
        print(data)
        print("post created successfully")


class ForSinglePost:
    @login_requried
    def get(self, *args, **kwargs):
        id = kwargs.get("id")
        qs = [p for p in posts if p.get("id") == id]
        return qs

    def put(self, id=None, *args, **kwargs):
        post = [p for p in posts if p.get("id") == id][0]
        title = kwargs.get("title")
        body = kwargs.get("body")
        post["title"] = title
        post["body"] = body
        print(post)


sign = SignInView()
sign.post(username="Bret", email="Sincere@april.biz")
pst = PostCreateView()
pst.post(title="mypost", body="this is my new post")
mp = MyPostView()
print(mp.get())
detail = ForSinglePost()
print(detail.get(id=5))
detail.put(id=5, title="my post", body="this my post")
# print(dir(dict))#to get the value in "dict"
