# ============================================================
# WEEK 01 | Daily Practice
# ============================================================

# ---------- DAY 01 (DD Mon YYYY) ----------

# Source: Claude (Warm-up) | Q1
# Question:  CREATING A CLASS OF PERSON AND PRINT HIS NAME AND AGE 
# Time Complexity: O(n)

# class Person (object):
#     def __init__(self,age,name):
#         self.age= age
#         self.name = name
        

#     def __str__(self):
        
#         print(f'name = {self.name} : age = {self.age}')

# p1 = Person(18,'shivam')
# print(p1.name)
# print(p1)


## Source: Claude (Warm-up) | Q2
## Question: CREATING A CLASS OF CIRCLE AND CALCULATE HIS AREA : 

# class Circle(object):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):

#         return (3.14*(self.radius)**2)

# c1 = Circle(2)
# print(c1.area())

## Source: Claude (Warm-up) | Q3
## Question: CREATING A CLASS "BANK ACCOUNT" WITH ATTRIBUTE ACOUNT_NUMBER AND BALANCE CREATE A INSTANCE OF 
## OF CLASS AND DEPOSIT AN AMMOUNT OF MONEY INTO ACCOUNT AND PRINT THE CURRENT BALANCE

# class BankAccount:
#     def __init__(self,An,bal):
#         self.account_number = An
#         self.balance = bal

#     def deposit(self, amount):
#         cb = self.balance + amount
#         return f'current balance = {cb}'

#     def setNewBalance(self):
#        pass

# # BETTER WAY TO ASKED ACCOUNT NO AND BALANCE FROM USER :
# accountnumber = int(input("Enter your account number :"))
# balance = int(input("Set the initial amount of your account :"))
# amount = int(input("enter the amount you want to deposit from your account :"))
# a1 = BankAccount(accountnumber,balance)
# print(a1.balance)
# print(a1.account_number)
# print(a1.deposit(amount))
# print(a1.balance)




