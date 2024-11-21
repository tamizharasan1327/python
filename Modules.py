def mod(a,b):
    quotient=0
    m=0
    result=0
    quotient=a//b
    m=quotient*b
    result=a-m
    print
    return result
def main():
    choice=1
    while choice!=0:
        print("Consider the Format")
        print("a mod b")
        a=int(input("Enter the value for a:"))
        b=int(input("Enter the value for b:"))
        res=mod(a,b)
        print(f"{a}mod{b}={res}")
        print("enter the choice 1 to continue and 0 to quit")
        choice=int(input("Enter the choice:"))
    print("Good Bye")
if __name__=="__main__":
    main()
