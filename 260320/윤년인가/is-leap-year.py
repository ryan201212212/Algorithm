Y= int(input())

if Y % 4 == 0 :
    print("true")

elif Y % 4 != 0 or (Y % 4 == 0 and Y % 100 == 0 and Y % 400 != 0):
    print("false")