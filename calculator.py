def script():
    print ("Welcome To M Techy Development Calculator Made By Manjeet Singh")

    print('''List Of Fumction Which Can You Use In This Calculator
    1. Adding
    2. Subtraction
    3. Division
    4. Mltiplication
    "For Example" If You Use Adding Simply type "1" And Press Enter''')
    a = int(input("Enter The Serial Number Which You Use"))
    print ("Ok Got It !!!!")
    
    
    
    if a == 1:
        print("You Select Addition Function")
        ad1 = int(input("Enter Your First Value To Addition"))
        ad2 = int(input("Enter The Secound Value To Addition"))
        admain = (ad1 + ad2)
        print("Your Added Number Is :-" , admain)
        # restart = input("Would You Like To Restart If Yes Type 'Yes' If No Type 'No' !!!!").lower()
    
    
    
    
    if a == 2:
        print("You Select Subtration")
        sub1 = int(input("Enter Your First Value For Subtraction"))
        sub2 = int(input("Enter Your Secound Value For Subtraction"))
        submain = (sub1 - sub2)
        print("Your Subtracted Value Is :-" , submain)
        # restart = input("Would You Like To Restart If Yes Type 'Yes' If No Type 'No' !!!!").lower()


    if a == 3:
        print("You Select Divison")
        div1 = int(input("Enter First Value For Divison"))
        div2 = int(input("Enter Your Secound Value For Divison"))
        divmain = (div1 / div2)
        print("Your Divided Value Is :-" , divmain)
        # restart = input("Would You Like To Restart If Yes Type 'Yes' If No Type 'No' !!!!").lower()

    if a == 4:
        print("You Select Multiplication")
        mtp1 = int(input("Enter Your First Value For Multiplication"))
        mtp2 = int(input("Enter Your Secound Value For Multiplication"))
        mtpmain = (mtp1 * mtp2)
        print("Your Multiplied Number Is :-" , mtpmain)
        # restart = input("Would You Like To Restart If Yes Type 'Yes' If No Type 'No' !!!!").lower()


    restart = int(input("Would You Like To Restart If Yes Type '1' If No Type '0'"))
    if restart == 1:
        script()
    if restart == 0:
        print("Thanks For Using Our Service Gretting From Manjeet Singh")
    
    else:
        print("Invalid Input Found Please Enter Valid Input")

    # help = input("")
    # if help == "Help":
    #     print("Ok I Got It You Need Help")
    #     print(restart)
script()