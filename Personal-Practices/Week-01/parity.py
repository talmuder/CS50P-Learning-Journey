#define main function
def main():
    x=int(input("What's x ? "))
    if is_even(x):
        print("EVEN")
    else:
        print("ODD")
#define is even funtion
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
#main program
main()