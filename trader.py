#定義fee函數
def fee(position):
    if position>1000000:
        tradingfee=0.005
    else:
        tradingfee=0.01
    n=position*tradingfee
    return n

#定義main函數
def main():
    p=float(input("How much money do you want to bulid a position? "))
    total=round(p+fee(p),2)
    print(f"您的購買總成本為：{total:,.2f}元")

#主程式
main()
