#定義階梯函數
def tierrate(position):
    if position>=1_000_000:
        return 0.001
    elif 100_000<=position<=999_999:
        return 0.005
    else:
        return 0.01

#定義手續費函數
def finalfee(position):
    return position*tierrate(position)

#定義main函數
def main():
    position=float(input("How much money do u want to bulid your position? "))
    cost=round(position+finalfee(position),3)
    finaltierfee=tierrate(position)*100
    print(f"您的交易等級費率為：{finaltierfee}％，總購買成本為{cost:,.3f}元")


#主程式
main()
