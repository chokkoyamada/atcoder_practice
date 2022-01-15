# A - Weird Function

# 特に問題ない。普通に関数定義してそれを問題通りに呼び出すだけ。

# 以下はコンテスト中の自分のコード。

def f(t):
    return t ** 2 + 2 * t + 3


t = int(input())
print(f(f(f(t) + t) + f(f(t))))
