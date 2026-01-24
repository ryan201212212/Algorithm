A = int(input())
age = int(input())

if A == 0 and age >= 19 :
    print("MAN")
elif A != 0 and age >= 19 :
    print("WOMAN")
elif A == 1 and age < 19 :
    print("BOY")
else :
    print("GIRL")