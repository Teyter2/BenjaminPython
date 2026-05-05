M=120000
S=25000
edad=int(input("ingrese su edad: "))
plan=int(input("""
-Elija un Plan-
1.Basico
2.Pro
3.Elite
 """))

match plan:
    case 1:
        if edad<=25:
            print("",)
        elif edad>=26:
            print("",)
    case 2:
        if edad<=25:
            print("",M*0.20)
        else:
            print("",)
    case 3:
        if edad<=25:
            print("",M*0.20)
        else:
            print("",)