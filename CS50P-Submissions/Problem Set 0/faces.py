#define main function
def main():
    n=input()
    print(convert(n))

#define convert function
def convert(n):
    return n.replace(":)", "🙂").replace(":(", "🙁")

#主程式
main()