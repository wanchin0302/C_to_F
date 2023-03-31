height = int(input("請輸入金字塔的高度: "))

# 控制行數
for i in range(1, height+1):
    # 控制列數
    for j in range(1, height-i+1):
        print(" ", end="")
    # 控制星號數量
    for k in range(1, 2*i):
        print("*", end="")
    print()