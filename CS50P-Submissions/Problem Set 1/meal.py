#define main funtion
def main():
    time = input("What time is it ? ").strip()
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")
    else:
        print("")

#define convert funtion
def convert(time):
    hours,minutes=time.split(":")
    h=float(hours)
    m=float(minutes)/60
    return h+m

#main program
main()