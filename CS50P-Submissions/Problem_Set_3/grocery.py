#define main function
def main():
    item = {}

    while True:
        try:
            food = input().strip().upper()

            if food in item:
                item[food] += 1
            else:
                item[food] = 1

        except EOFError:
            print()
            break

    for i in sorted(item.keys()):
        print(item[i],i)

#main program
if __name__ == "__main__":
    main()