r=int(input("r= "))
m=input("kerakli parametrni kiring= ")
pi=3.14
match m:
    case "d":
        a=2*r
    case "s":
        a=pi*r**2
    case "l":
        a=2*pi*r
print(a)