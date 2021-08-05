def full_adder(cin, a , b): #adder has three inputs
       
    sum_ = (a ^ b) ^ cin
    cout = (cin & a) | (cin & b) | (a & b)
    return [cout,sum_] 

def bit_addition(a, b):#8 bit addition of two numbers
    carry = 0
    addl = [0,0,0,0,0,0,0,0] #stores the list of binary addition
    for i in range (7 , -1 ,-1):
        addl[i] = full_adder(carry, a[i], b[i])[1]
        carry = full_adder(carry, a[i], b[i])[0]
        
   
    return(addl) #returns the binary value in list 
  


def bitwise_addition(a,b): #bitwise addition of two numbers
    carry = a & b   
    sum_ = a ^ b
    while carry > 0:
        shift_left = carry << 1
        carry = sum_ & (carry << 1)
        sum_ = sum_ ^ shift_left   
    return sum_  #returns the sum
