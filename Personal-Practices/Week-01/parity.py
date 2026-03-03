#define main function
def main():
    x=int(input("What's x ? "))
    if is_even(x):
        print("EVEN")
    else:
        print("ODD")
#define is even funtion
def is_even(n):
        return True if n % 2 == 0 else False
#main program
main()