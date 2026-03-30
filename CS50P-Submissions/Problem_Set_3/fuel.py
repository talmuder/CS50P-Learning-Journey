#define main function
def main():
    print(fuel())

#define fuel function
def fuel():
      while True:
        n = input("Fraction: ")
        try:
            x , y = n.split("/")
            x = int(x)
            y = int(y)

            if x > y :
                continue

            p = round((x / y *100))

            if p <= 1 :
                return "E"
            elif p >= 99 :
                return "F"
            else:
                return f"{p}%" 
        except (ValueError,ZeroDivisionError):
            pass

#main program
if __name__ =="__main__":
    main()