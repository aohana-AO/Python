import random

print("数あてゲームを開始します。\n難易度を選択してください\nレベル１： 回答数３０\nレベル２： 回答数２０\nレベル３： 回答数１０\nレベル４： 回答数５\nレベル５： 回答数１\n")
nyuuryoku2 = 0
x = 0
y = 0
nyuuryoku = int(input("難易度レベル："))
if nyuuryoku == 1:
    nyuuryoku2 = 30
elif nyuuryoku == 2:
    nyuuryoku2 = 20
elif nyuuryoku == 3:
    nyuuryoku2 = 10
elif nyuuryoku == 4:
    nyuuryoku2 = 5
else:
    nyuuryoku2 = 1

kotae = random.randint(50, 100)

for i in range(nyuuryoku2):
    x += 1
    kazu = int(input("１０から９９の数字を入力してください："))
    if kazu < kotae:
        print("もっと大きい数です")
    elif kazu > kotae:
        print("もっと小さい数です")
    else:
        print(str(x)+"回目で正解しました")
        y = 1
        break

if y == 1:
    print("さすがです！！")
else:
    print("残念・・")
