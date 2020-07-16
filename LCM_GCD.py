import math

def Lcm(num1):
    lcm=num1[0]
    for i in range(1,len(num1)):
        lcm=lcm*num1[i]//math.gcd(lcm,num1[i])
    return lcm

def lcmgcd():
    while True:
        print("Enter 1 for LCM and GCD of Two numbers\nEnter 2 for LCM and GCD of Three numbers\nEnter 3 for back")
        k=input("Enter here:")
        try:    
            key=int(k)
        except:
            print("Invalid key!")
        
        if key==1:
            A=input("Enter first number:")
            B=input("Enter second number:")
            try:
                a=int(A)
                b=int(B)
            except:
                print("Error!")
                break
            if a==0 or b==0:
                print("Zero not allowed!")
                break
            gcd=math.gcd(a,b)
            print("GCD is:",gcd)
            print("LCM is:",int((int(A)*int(B))/gcd))
            if key==2:
                num=[]
                A=input("Enter first number:")
                B=input("Enter second number:")
                C=input("Enter third number:")
                try:
                    a=int(A)
                    b=int(B)
                    c=int(C)
                except:
                    print("Error!")
                    break
                if a==0 or b==0 or c==0:
                    print("Zero not allowed!")
                    break
                num.append(a)
                num.append(b)
                num.append(c)
        
                g=math.gcd(a,b)
                gcd=math.gcd(g,c)
                print("GCD is:",gcd)
                print("LCM is:",Lcm(num))
            if key==3:
                break
            else:
                print("Enter correct key!")
                break
