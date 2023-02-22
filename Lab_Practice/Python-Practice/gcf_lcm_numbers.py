""" Write a function that returns the greatest common factor or least common multiple of two numbers. 
The user can choose whether he wants the greatest common divisor, the least common multiple, 
or both. """


def gcf_number(x,y):
    """ Returns the greatest common factor of x and y."""
    if x < y:
       smaller = x
    else:
       smaller = y
       
    while(True):
       if((x % smaller == 0) and (y % smaller== 0)):
           GCF = smaller
           break
       smaller -= 1

    return GCF

def lcm_number(x,y):
    """ Returns the least common multiple of x and y. """
    if x > y:
       greater = x
    else:
       greater = y
       
    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           LCM = greater
           break
       greater += 1

    return LCM


def gcf_lcm_numbers(x,y,choice):
    """ This functions returns the output as per the user choice."""

    if choice==1:
        LCM = lcm_number(x,y)
        return LCM
    elif choice==2:
        GCF = gcf_number(x,y)
        return GCF
    else:
        LCM = lcm_number(x,y)
        GCF = gcf_number(x,y)
        return LCM, GCF


def main():
    
    x = int(input("Enter the number:     "))
    y = int(input("Enter the number:     "))
    choice = int(input("Choose what you want:\n1 --> Least Common Multiple.\n2 --> Greatest Common Factor\n3 --> Both\nEnter your choice:    "))
    
    if x<0 or y<0 or choice<1 or choice>3:
        print("Please enter positive intiger.")
        main()
    else:
        Result =  gcf_lcm_numbers(x,y,choice)
        
        if choice==1:
            print(f"LCM of {x} & {y} is {Result}")
        elif choice==2:
            print(f"GCf of {x} & {y} is {Result}")
        else:
            print(f"LCM of {x} & {y} is {Result[0]}\nGCf of {x} & {y} is {Result[1]}")
            
        

if __name__ == '__main__':
    main()