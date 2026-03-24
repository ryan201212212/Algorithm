A, B = map(int, input().split())

r = A % B
print(A // B, end='.')

for _ in range(20):
    r *= 10
    print(r // B, end='')
    r %= B