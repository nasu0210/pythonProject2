#3154
N = int(input())  # 플레이어 수를 입력받습니다.
scores = []  # 각 플레이어의 점수를 저장할 리스트를 생성합니다.
for _ in range(N):
    game_scores = list(map(int, input().split()))  # 각 게임에서의 점수를 입력받습니다.
    scores.append(game_scores)
tli=[]
for m in zip(*scores):
    li = []
    for i in m:
        if m.count(i) > 1:
            li.append(0)
        else:
            li.append(i)
    tli.append(li)
k=list(zip(tli))
for i in k:
    print(sum(i))