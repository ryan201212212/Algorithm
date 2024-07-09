N = int(input()) #참가자 수 입력
S, M, L, XL, XXL, XXXL = map(int, input().split()) #티셔츠 사이즈별 신청자 수 공백으로 구분하여 입력
T, P = map(int, input().split()) # T,P 묶음 수 공백으로 구분하여 입력

t_bundles = 0
for i in [S, M, L, XL, XXL, XXXL] :
    t_bundles += (i + T - 1) // T
#t_shirts = S + M + L + XL + XXL + XXXL
#t_bundles = (t_shirts + T - 1) // T

P_bundles = N // P
indi_P = N % P

print(t_bundles)
print(P_bundles, indi_P)