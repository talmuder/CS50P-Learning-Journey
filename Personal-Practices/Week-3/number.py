#define main function
def main():
    x = get_number("What's x ? ")
    print(f"X is {x}")

#define get number function
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Your enter is not an Integer, Please Enter Again the "X" ')

#main program
if __name__ == "__main__":
    main()