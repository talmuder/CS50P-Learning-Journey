# define check market function
def get_user_target():
    while True:
        try:
            target = float(input("請輸入你的目標成交價 (Target Price): "))
            if target > 0:
                return target
            print("請輸入正數。")
        except ValueError:
            print("錯誤：請輸入數字。")

# define main function
def main():
    market_prices = [68000, 69500, 71000, 70500, 72000]
    
    my_target = get_user_target()
    
    found = False
    for price in market_prices:
        if price >= my_target:
            print(f"目標達成！成交價：{price}")
            found = True
            break 
    
    if not found:
        print("今日市場價格皆未達標。")

if __name__ == "__main__":
    main()