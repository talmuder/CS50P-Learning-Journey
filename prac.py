#定義清理文字函數
def clean(text):
    return text.strip().replace(" ","_").upper()

#定義手續費階梯函數
def discount(amount):
    if amount>=1_000_000:
        return 0.001
    elif amount>=100_000:
        return 0.005
    else:
        return 0.01

#定義main函數
def main():
    asset=input("請輸入交易指令(如 BUY BTC)")
    amount=float(input("請輸入交易金額"))
    fee=round(amount*discount(amount),3)
    print(clean(asset))
    print(f"預估手續費為{fee:,.3f}")

#主程式
main()
