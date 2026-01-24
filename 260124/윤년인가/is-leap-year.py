Y = int(input())

if Y%100 == 0 :
    print("false")
elif Y%400 == 0 : 
    print("true")
elif Y % 4 == 0 :
    print("true")
elif Y % 4 != 0 :
    print("false")
