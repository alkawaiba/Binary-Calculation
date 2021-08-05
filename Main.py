#importing the modules to main module
import Inputs
import DectoBin
import adder

def ltost(li):
    #converting the list into string to make it easier to add the binary numbers
    string = ""
    for i in li:
        i = str(i)
        string = string + i
    return string 

answer = "yes"

while answer != "no":
    if answer == "yes":
        li = Inputs.number()
        binary1 = DectoBin.binary_conv(li[0])    
        binary2 = DectoBin.binary_conv(li[1])       
        bit_addition = adder.bit_addition(binary1, binary2)
        
        #displaying the output
        print("The binary value of first number is: ", ltost(binary1))
        print("The binary value of second number is ", ltost(binary2))        
        print("The binary addition is: ",ltost(bit_addition))

        
    answer = input("\nDo you want to do conntinue?yes/no: ").lower()#checking if the user wants to continue or not    

if answer == "no":
    print("\nThank you for using Bit Adder.")#terminating the program as per user's choice
        
        
