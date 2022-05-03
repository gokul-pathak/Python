def mainMenu():
    print("SELECT A FUNCTION")
    print(" ")
    print("e1- Calculate The Area Of A Sphere")
    print("e2- Calculate The Volume Of A Cube")
    print("e3- Multiplication Table")
    print("e4- Converting Negatives To Positives")
    print("e5- Average Student Grades")
    print("e6- Car Sticker Color")
    print("e7- Exit")
    print(" ")

    while True:

        selection = input("Enter a choice: ")

        if(selection == "e1"):
            e1()
            break
        elif(selection == "e2"):
            e2()
            break
        elif(selection == "e3"):
            e3()
            break
        elif(selection == "e4"):
            e4()
            break
        elif(selection == "e5"):
            e5()
            break
        elif(selection == "e6"):
            e6()
            break
        elif(selection == "e7"):
            print("Goodbye")
            break
        else:
            print("Invalid choice. Enter 'e1'-'e7'")
            print("")


mainMenu()