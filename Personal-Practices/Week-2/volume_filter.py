#define stock screener function
def stock_screener(stocks,prices,volumes):

    count = 0
    total_volume = 0

    for i in range(len(stocks)):
        if prices[i] > 150 and volumes[i] > 10000:
            print(f"符合條件的股票: {stocks[i]}")
            count = count + 1
            total_volume = total_volume + volumes[i]
    print(f"符合條件的股票數量: {count}")
    print(f"符合條件的股票的總成交量: {total_volume}")

    for i in range(len(stocks)):
        if volumes[i] > 20000:
            print(f"第一檔爆量股票: {stocks[i]}")
            break

    max_volume = volumes[0]
    max_stock = stocks[0]

    for i in range(len(stocks)):
        if volumes[i] > max_volume :
            max_volume = volumes[i]
            max_stock = stocks[i]
    print(f"成交量最大的股票: {max_stock}",f"最大成交量: {max_volume}",sep = "\n")

#main program
if __name__ == "__main__":

    stocks = ["AAPL","TSLA","NVDA","AMD","META"]
    prices = [175,245,920,110,480]
    volumes = [8000,18000,25000,12000,9000]
    
    stock_screener(stocks,prices,volumes)