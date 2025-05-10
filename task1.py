# Напишите алгоритм поиска в глубину (DFS)
#
# Формат входных данных:
# Граф задаётся в виде словаря, где ключи — вершины, а значения — списки смежных вершин.
#
# Обход начинается с заданной стартовой вершины.
# Требуется:
# 1.Реализовать DFS (Depth-First Search) — обход графа в глубину.
# 2.Вернуть список вершин в порядке их посещения.

# Пример входных данных
# graph = {
#     1: [2, 3],
#     2: [1, 4],
#     3: [1, 5],
#     4: [2],
#     5: [3]
# }
# start = 1
#
# Пример выходных данных
# [1, 2, 4, 3, 5]  # Возможен и другой порядок, зависящий от реализации DFS
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}
start = 1
path = []
maxi=0
def rec1(delta_path):
    path_max = delta_path
    delta_path2=[]
    print(path_max, delta_path2, delta_path)
    for i in graph[delta_path[-1]]:
        print(i)
        if i not in delta_path:
            delta_path.append(i)
            delta_path2=rec1(delta_path).copy()
            print("RETURN:", delta_path2)
            delta_path.pop()
            # print("d", delta_path, "d2", delta_path2, "l1", len(delta_path), "l2", len(delta_path2))
            if len(delta_path2) > len(path_max):
                path_max=delta_path2.copy()
                # print("APOFJO", path_max,"", delta_path2)
    print("RETURN:", path_max)
    return path_max
def rec2(delta_path, current_i):
    if current_i==-1 or len(delta_path)==len(graph):
        return delta_path
    for i in graph[delta_path[current_i]]:
        if i not in delta_path:
            delta_path.append(i)
            current_i=len(delta_path)-1
            return rec2(delta_path, current_i)
    current_i-=1
    return rec2(delta_path, current_i)


print("EXIT:", rec2([start], 0))
