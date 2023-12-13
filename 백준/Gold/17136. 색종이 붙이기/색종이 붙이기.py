array = []
for _ in range(10):
    array.append(list(map(int, input().split())))

def max_size(x, y):
    for size in range(5, 0, -1):
        if x + size > 10 or y + size > 10:
            continue
        if all(array[i][j] == 1 for i in range(x, x + size) for j in range(y, y + size)):
            return size
    return 0

def change_array(x, y, size, value):
    for i in range(size):
        for j in range(size):
            array[x + i][y + j] = value

def dfs(paper_count):
    results = []
    possi = False
    for i in range(10):
        for j in range(10):
            if array[i][j] == 1:
                max_s = max_size(i, j)
                for size in range(max_s, 0, -1):
                    if paper_count[size] > 0:
                        change_array(i, j, size, 0)
                        paper_count[size] -= 1
                        result = dfs(paper_count)
                        if result != -1:
                            results.append(result+1)
                            possi = True
                        paper_count[size] += 1
                        change_array(i, j, size, 1)
                if possi:
                    return min(results)
                return -1
    return 0

print(dfs([0, 5, 5, 5, 5, 5]))
