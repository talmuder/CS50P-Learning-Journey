#define main function
def main():
    plate = input("Plate: ").strip()
    
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#define is_valid function
def is_valid(plate):
    if not 2 <= len(plate) <= 6:
        return False

    if not plate[0:2].isalpha():
        return False

    if not plate.isalnum():
        return False

    found_number = False

    for i in range(len(plate)):
        if plate[i].isdigit():
            if not found_number:
                found_number = True
                if plate[i] == "0":
                    return False
        else:
            if found_number:
                return False
    return True
    
#main program
if __name__ == "__main__" :
    main()