# Даны N городов и M дорог между ними. Дороги двусторонние (граф неориентированный). 
# Известно, что города разделены на группы (острова), 
# между которыми дорог нет. То есть граф состоит из нескольких компонент связности (островов). 
# Необходимо ответить на следующие вопросы:
# 
# 1. Есть ли путь между двумя заданными городами (вершинами)?
# 2. Сколько всего островов (компонент связности) в графе?
# 3.Перечислить, какие города принадлежат каждому острову.
# 
# Входные данные:
# Первая строка: N (количество городов) и M (количество дорог).
# Следующие M строк: пары чисел u и v, обозначающие дорогу между городами u и v.
# Затем вводится два числа: start и end — номера городов, между которыми нужно проверить наличие пути.
# 
# Выходные данные:
# Ответ на вопрос, есть ли путь между start и end ("YES" или "NO").
# Количество островов (компонент связности) в графе.
# Список городов для каждого острова (в порядке возрастания номеров островов).

# Пример 1:
# 5 3
# 1 2
# 2 3
# 4 5
# 1 4
# 
# Ожидаемый вывод:
# 
# NO
# 2
# 1: [1, 2, 3]
# 2: [4, 5]

# Пример 2:
# 6 4
# 1 2
# 3 4
# 5 6
# 2 3
# 3 5
# 
# Ожидаемый вывод:
# 
# YES
# 1
# 1: [1, 2, 3, 4, 5, 6]

# Пример 3:
# 7 0
# 1 2
# 
# Ожидаемый вывод:
# 
# NO
# 7
# 1: [1]
# 2: [2]
# 3: [3]
# 4: [4]
# 5: [5]
# 6: [6]
# 7: [7]

n, m = map(int, input("Inter N&M: ").split())
graph={}
for i in range(1,n+1):
    graph[i]=[]
for i in range(m):
    a, b = map(int, input("Inter 2 cities: ").split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
start, end = map(int, input("Inter start&end: ").split())


def rec(delta_path, current_i):
    if delta_path[-1]==end:
        return delta_path
    if current_i==-1:
        return "NO!"
    for i in graph[delta_path[current_i]]:
        if i not in delta_path:
            delta_path.append(i)
            current_i=len(delta_path)-1
            return rec(delta_path, current_i)
    current_i-=1
    return rec(delta_path, current_i)
print("EXIT:", rec([start], 0))
lands={
    # 1:[]
}
def rec1(delta_path):
    path_max = delta_path
    delta_path2=[]
    # print(path_max, delta_path2, delta_path)
    for i in graph[delta_path[-1]]:
        # print(i)
        if i not in delta_path:
            delta_path.append(i)
            delta_path2=rec1(delta_path).copy()
            # print("RETURN:", delta_path2)
            delta_path.pop()
            # print("d", delta_path, "d2", delta_path2, "l1", len(delta_path), "l2", len(delta_path2))
            if len(delta_path2) > len(path_max):
                path_max=delta_path2.copy()
                # print("APOFJO", path_max,"", delta_path2)
    # print("RETURN:", path_max)
    return path_max
def rec2():
    starty=1
    lands[1]=rec1([starty])
    for i in graph:
        o=True
        for j in lands:
            if i in lands[j]:
                o=False
                break
        if o:
            lands[len(lands)+1]=rec1([i])
        # print(lands)
    return lands
# print("EXIT:", rec2())
print("EXIT: ")
landy=rec2()
for i in landy:
    print(str(i)+":", *landy[i])