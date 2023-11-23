class Node:
    def __init__(self, idx):
        self.idx = idx
        self.prev = None
        self.next = None

def solution(n, k, cmd):
    table = [Node(i) for i in range(n)]
    for i in range(1,n):
        table[i].prev = table[i-1]
    for i in range(n-1):
        table[i].next = table[i+1]
    current_row = table[k]
    deleted_rows = []

    for command in cmd:
        if command[0] == 'U':
            x = int(command.split()[1])
            for _ in range(x):
                if current_row.prev:
                    current_row = current_row.prev
        elif command[0] == 'D':
            x = int(command.split()[1])
            for _ in range(x):
                if current_row.next:
                    current_row = current_row.next
        elif command[0] == 'C':
            deleted_rows.append(current_row)
            prev_row = current_row.prev
            next_row = current_row.next
            if prev_row:
                prev_row.next = next_row
            if next_row:
                next_row.prev = prev_row
            if not next_row:
                current_row = prev_row
            else:
                current_row = next_row
        elif command[0] == 'Z':
            row_to_restore = deleted_rows.pop()
            prev_row = row_to_restore.prev
            next_row = row_to_restore.next
            if prev_row:
                prev_row.next = row_to_restore
            if next_row:
                next_row.prev = row_to_restore

    result = ['O'] * n
    for row in deleted_rows:
        result[row.idx] = 'X'

    return ''.join(result)
