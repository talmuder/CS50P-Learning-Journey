#define main function
def main():
    user_input = input("Input: ").strip()

    word = ["a","e","i","o","u"]

    print("Output: ",end = "")

    for enter in user_input:
        if enter.lower() not in word:
            print(enter,end = "")
    print()

#main program
if __name__ == "__main__":
    main()