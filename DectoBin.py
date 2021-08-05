def binary_conv(num):#converting decimal number to 8 bit binary number 
    #making two lists
    binary = []
    actual_binary =[]
    #making count as 0
    count = 0
    while (count != 8):#Loop is continued while count is not equals to 8
        remainder = num%2 #Making a variable named remainder and placing the modular value of num
        binary.append(remainder)#Adding the remainder in binary as a list 
        num = int(num//2)#Swapping new num as the int value of num divided by 2
        count += 1#Increasing the value of count by 1
    for i in range(len(binary)-1,-1,-1):#Reversing the list and adding to actual binary 
        actual_binary.append(binary[i])
    return actual_binary#Returning the actual binary in a list
      
    


