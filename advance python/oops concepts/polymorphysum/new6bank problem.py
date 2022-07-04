#class:Bank  ...to creat 3 methodes
#1..account creation:name,account no,minimumbalance
#2..withderowel:balance amount
#3..deposit:balace amount

class Bank:
    bank_name="SBI"
    minimumbal=500
    total_bal=20000
    def account_creation(self,name,account_no):
        self.name=name
        self.account_no=account_no
        print("acc name",self.name,"account number",self.account_no)
    def withdrowel(self,bala_amount):
        self.bala_amount=bala_amount
        if(self.bala_amount>Bank.total_bal):
            print("insufficient balance")
        else:
            print("account has been debited", self.bala_amount, "balance  amount", Bank.total_bal - self.bala_amount)
    def deposit(self,last_balce):
       self.last_balce=last_balce

       print("total balance",Bank.total_bal+self.last_balce)
ob=Bank()
ob.account_creation("DEEGO",1234565)
ob.withdrowel(25000)
ob.deposit(5000)
                  #or
