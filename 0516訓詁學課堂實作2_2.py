# -*- coding: utf-8 -*-
"""0516訓詁學課堂實作2-2
## 課堂練習

2. 請寫一個 `is_odd(x)` 函式，檢查輸入的參數 `x` 是不是奇數。如果 `x` 是奇數則回傳 `Ture`；若 `x` 不是奇數則回傳 `False`。

def is_odd(x):
    if x % 2 != 0:
        return True
    else:
        return False

x = int(input("請輸入任一整數: "))
result = is_odd(x)
print(result)