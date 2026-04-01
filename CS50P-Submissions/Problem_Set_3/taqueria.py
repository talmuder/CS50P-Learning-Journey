#define main function
def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    ask(menu)

#define ask function
def ask(menu):
    cost = 0

    while True:
        
        try:
            food = input("Item: ").strip().title()
            if food in menu:
                cost += menu[food]
                print(f"Total: ${cost:.2f}")

        except EOFError:
            print()
            break
#main program
if __name__ == "__main__":
    main()