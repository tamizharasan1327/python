#import os
#os.system('cls')
#def clearscreen():
#    print("\n"*60)
def main():
    #clearscreen()
    print("reverse the number")
    list1=[int(x) for x in input("enter the number separate by space:").split()]
    print(f"orginal format:{list1}'")
    list1.sort()
    print(f"sorted list {list1}")
    list1.reverse()
    print(f"reverse inbuild function :{list1}")
    list2=list1[::-1]
    print(f"reverse the list without inbuild function :'{list2}'")
    print("................end................")
    print("sort in descending order using sorted function")
    list3=sorted(list1,reverse=True)
    print(f"Descending order:{list3}")
    list1.sort(reverse=True)
    print(f"Descending order with sort function:")
    print(f"Desecding order: {list1}")
if __name__=='__main__':
    main()
