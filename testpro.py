Fname=[]
Lname=[]
Gender=[]
Address=[]
Contact_no=[]
Chitizenship_no=[]
username=[]
password=[]
re_password=[]
print("Enter your First name: ")
first=input()
Fname.append(first)

print("Enter your last name: ")
last=input()
Lname.append(last)

print("Enter your Gender: ")
g=input()
Gender.append(g)

print("Enter your Address: ")
a=input()
Address.append(a)

print("Enter your contact no.: ")
c=input()
Contact_no.append(c)

print("Enter your citizenship number.: ")
ci=input()
Chitizenship_no.append(ci)

print("Enter a username for your account: ")
us=input()
username.append(us)

print("Create new password for your account(please remember your password).: ")
ps=input()
password.append(ps)

print("confirm your password.: ")
rs=input()
re_password.append(rs)

if(password == re_password):
    print("\tcongratulation your account is successfully created!!")
else:
    print("\tPassword did not match please try again later!!")
print("You entered following data: ")
print("Your full name is:",Lname+Fname)
print("Gender:",Gender)
print("Address: ",Address)
print("Contact NO.",Contact_no)
print("Chitizen NO.",Chitizenship_no)
print("Username:",username)
print("Your password is",password)
'''
print("\tEnter your first name: \t")
    fname=input()
    print("\tEnter your surname: \t")
    sname=input()
    print("\tEnter your gender: \t")
    gender=input()
    print("\tEnter your address: \t")
    address=input()
    print("\tEnter your contact no. : \t")
    contact_no= int(input())
    print("\tCreate a new password(*Create strong password): ")
    password=input()
    print("Re-enter your passsword(*Note remeber your password): ")
    re_password=input()
    if(password==re_password):
        print("\tcongratulation your account is successfully created!!")
    else:
        print("\tPassword did not match please try again later!!")
        '''