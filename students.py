secA=[]
Anoofstudents=int(input("no. of student for secA"))
secB=[]
Bnoofstudents=int(input("no. of student for secb"))
for i in range(Anoofstudents):
    inputsecA=input("Enter a student name secA: ")
    secA.append(inputsecA)
for i in range(Bnoofstudents):
    inputsecB=input("Enter a student name secB: ")
    secB.append(inputsecB)
institue=[secA,secB]
for i in range(len(institue)):
    if i==0:
        print("the list of secA student are: ")
    else:
        print("the list of secB students are: ")
    for j in range(len(institue[i])):
        print(institue[i][j])
