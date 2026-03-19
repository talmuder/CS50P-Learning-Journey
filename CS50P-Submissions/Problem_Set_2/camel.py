#define main function
def main():
    camel = input("camelCase: ").strip()
    print("snake_case: ",end = "")

    for i in camel:
        if i.isupper():
            print("_" + i.lower(),end = "")
        else:
            print(i,end="")
    print()

#main program
if __name__ == "__main__":
    main()