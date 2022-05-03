salary=int(input("enter your salary here: "))
if(salary<=20000 and salary>30000):
    tax=0.15*salary
    netsalary=salary-tax
    print("the salary after deduction tax is:",netsalary)
elif(salary<=30000 and salary>40000):
    tax=0.2*salary
    netsalary=salary-tax
    print("the salary after deduction tax is:",netsalary)
elif(salary<=40000 and salary>50000):
    tax=0.25*salary
    netsalary=salary-tax
    print("the salary after deduction tax is:",netsalary)
elif(salary<=50000):
    tax=0.3*salary
    netsalary=salary-tax
    print("the salary after deduction tax is:",netsalary)
else:
    print("invalid input:")