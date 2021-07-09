n = int(input())
result = 0
score = input().split()
for i in range(len(score)): score[i] = int(score[i])
M = max(score)
for i in range(len(score)): result += score[i] / M * 100
print(result / n)