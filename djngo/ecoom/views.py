from djngo.blog.models import users
from djngo.ecoom.models import product,carts

def athentification(**kwargs):
    user_name=kwargs.get("username")
    product_name=kwargs.get("id")
    use=[users for i in users if i["username"]==user_name]
    pro=[product for i in product if i["id"]==product_name]
    return use,pro
data=athentification(username="Bret",id=1001)
if data:
    print("login success")

else:
    print("login failed")