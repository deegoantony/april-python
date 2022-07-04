#current year
#crrent mont
#current date

#birt year
#birt mon
#birt day

#calculate the age

# crt_ye=int(input("enter the current year"))
# crt_mn=int(input("enter the current month"))
# crt_da=int(input("enter the current day"))
# bir_ye=int(input("enter the birth year"))
# bir_mn=int(input("enter the birth month"))
# bir_da=int(input("enter the birth day"))
# sum1=(crt_ye-bir_ye)-1
# sum2=(crt_ye-bir_ye)
# if(crt_mn==bir_mn)&(crt_da==bir_da):
#     print(sum2,"yeras old")
# elif(crt_mn==bir_mn)&(bir_da>crt_da):
#     print(sum2,"years and",bir_da,"days")
#
# else:
#      print(sum1,"years and",crt_mn,"months",crt_da,"days")

from datetime import date
def age(birthdate):
    today=date.today()
    one_zero=((today.month,today.day)<(birthdate.month,birthdate.day))
    yeardiffer=today.year-birthdate.year
    age=yeardiffer-one_zero
    return age
print(age(date(1994,10,1)))
