#define stock screener funtion
def stock_screener(stocks,prices,volumes):

    for price in prices:
        if price > 150:
            return price

    for volume in volumes:
        if volume > 10000:
            









#main program
if __name__ == "__main__":

    stocks = ["AAPL","TSLA","NVDA","AMD","META"]
    prices = [175,245,920,110,480]
    volumes = [8000,18000,25000,12000,9000]
