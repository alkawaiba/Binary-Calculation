def integer_check(num):
    #Exception Handling case
    try:
        int(num)    
        return True
    except ValueError:
        return False

#input values from the user    
def number():
    print("\nNOTE:You can only input numbers from 0 to 255\n")
    
    check1 = "no"
    check2 = "no"
    check3 = "no"
    

    while check3 == "no" :
        while check1 == "no" :
            input1 = input("Enter the first number: ") #checking the input error
            if integer_check(input1) == False:    
                print("Data Type ERROR!\nThe Program is meant to accept integer values only.\n")
            else:
                num1 = int(input1)
                if num1 > -1 and num1 < 256 : #checking the condition with input value
                    check1 = "yes"
                else:
                    print("Data Type ERROR!\nPlease enter a number between 0 and 255 only.\n")


        while check2 == "no" :
            input2 = input("Enter the second number: ") #checking the input error
            if integer_check(input2) == False:
                print("Data Type ERROR!\nThe Program is meant to accept integer values only.\n")
            else:
                num2 = int(input2)
                if num2 > -1 and num2 < 256 : #checking the condition with input value
                    check2 = "yes"
                else:
                    print("Data Type ERROR!\nPlease enter a number between 0 and 255 only.\n")

        #checking th necessary conditions to display the output
        if (num1 + num2) > 255 :
            print("The binary addition cannot exceed 255.Try again!")
            check1 = "no"
            check2 = "no"

        else:
            check3 = "yes"
            return[num1,num2] #returning the list of two numbers   


                
            
            

