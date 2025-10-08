# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    a, b = map(int, input().split())
    total_banok = a + b - 1  # общее количество банок (последняя общая)
    harry_promah = total_banok - a  # сколько не прострелил Гарри
    larry_promah = total_banok - b  # сколько не прострелил Ларри
    print(harry_promah, larry_promah)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()