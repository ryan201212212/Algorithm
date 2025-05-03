
A = int(input())
B = int(input())
C = int(input())

result = A + B - C

str_A = str(A)
str_B = str(B)
str_C = str(C)

str_result = str_A + str_B #여기서는 str_C를 제외한 것만 우선 합한다. 문자열에서의 합은 이어 붙이는 것
string_str_result = int(str_result) - int(str_C) # 이어붙인 str_result에서 int를 뺀다.

print(result)
print(string_str_result)
