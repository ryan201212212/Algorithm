N = int(input())
scores = list(map(int, input().split()))
A = max(scores)

B = [(score / A * 100) for score in scores]
Avg_score = sum(B) / N

print(Avg_score)