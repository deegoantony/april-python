# to generate an exception error

age=int(input("enter your age"))
if age>=18:
    print("eligible")
else:
    raise Exception ("not eligible")

