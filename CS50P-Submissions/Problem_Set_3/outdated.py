#define main function
def main():
    while True:
        date = input("Date: ").strip()

        try:
            if "/" in date:
                month,day,year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if  not (1 <= month <= 12 or 1 <= day < 31):
                    raise ValueError

            elif "," in date:
                parts = date.split(" ")

                if len(parts) != 3:
                    raise ValueError

                month_name = parts[0]
                day = int(parts[1].strip(","))
                year = int(parts[2])

                if not 1 <= day <= 31:
                    raise ValueError

                if month_name in months:
                    month = months.index(month_name) + 1

            else:
                raise ValueError

            print(f"{year}-{month:02}-{day:02}")
            break

        except(ValueError,KeyError,IndexError):
            pass
#main program
if __name__ == "__main__":
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    main()