#define main function
def main():
    camel = input("camelCase: ").strip()
    print("snake_case: ",end = "")

    for i in camel:
        if i.isupper():
            print("_" + i.lower(),end = "")
        else:
            print(i)
            