x,y,z=input("Expression: ").strip().split()
newx=float(x)
newz=float(z)

match y:
    case "+":
        print(f"{newx+newz:.1f}")
    case "-":
        print(f"{newx-newz:.1f}")
    case "*":
        print(f"{newx*newz:.1f}")
    case "/":
       print(f"{newx/newz:.1f}")
    case _:
        print("Error")