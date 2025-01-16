import argparse
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--number1",help="first number")
    parser.add_argument("--number2",help="second number")
    parser.add_argument("--operation",help="operation",choices=["add","sub","mul"])
    args=parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)
    a=int(args.number1)
    b=int(args.number2)
    result=None
    if args.operation =="add":
        result=a+b
    elif args.operation=="sub":
        result=a-b
    elif args.operation=="mul":
        result=a*b
    else:
        print("enter the valid operator")
    print("Result:",result)
