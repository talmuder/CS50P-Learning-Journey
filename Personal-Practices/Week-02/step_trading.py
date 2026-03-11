#define check market function
def check_market():
    while True:
        today_price=float(input("Today's Price :"))
        if today_price > 0:
            return today_price
        else:
            print("Error, Please enter the Correct Price ")
        
#define main funtion
def main():
    market_prices = [68000, 69500, 71000, 70500, 72000]
    for market_price in market_prices:
        if market_price >= check_market():
            print(f"目標達成！成交價：{market_price}")
            break
        else:
            print("今日未達標")
            break

#main program
if __name__ == "__main__":
    main()