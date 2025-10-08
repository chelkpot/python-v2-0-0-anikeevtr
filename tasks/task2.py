# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    X, Y, Z = map(int, input().split())
    pencil_price = 3
    pen_price = pencil_price + 2  # 5 рублей
    marker_price = pen_price + 7  # 12 рублей
    total_cost = X * pencil_price + Y * pen_price + Z * marker_price
    print(total_cost)

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()