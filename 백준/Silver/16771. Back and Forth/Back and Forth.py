first_buckets = list(map(int, input().split()))
second_buckets = list(map(int, input().split()))
# 월요일 : 각 창고에 1000갤런씩 우유 채우기
# 화요일 : 1창고에서 1양동이 퍼서 2창고에 채워넣기. 양동이는 2창고에 있음
# 수요일 : 2창고에서 화요일에 갖다 놓은 양동이를 채워 1창고에 붓는다. 양동이는 1창고에 있음
# 목요일 : 1창고에서 수요일에 갖다 놓은 양동이를 채워 2창고에 붓는다. 양동이는 2창고에 있음
# 금요일 : 2창고에서 화요일이나 목요일에 갖다 놓은 양동이를 채워 1창고에 붓는다. 양동이는 1창고에 있음
lst = []
s = set()


def DFS(day):
    if day == 4:
        s.add(sum(lst))
        return
    if day%2 == 0:
        for i in range(10):
            FJ = first_buckets.pop(i)
            second_buckets.append(FJ)
            lst.append(-FJ)
            DFS(day+1)
            first_buckets.insert(i, second_buckets.pop())
            lst.pop()
    else:
        for i in range(10):
            FJ = second_buckets.pop(i)
            first_buckets.append(FJ)
            lst.append(FJ)
            DFS(day+1)
            second_buckets.insert(i, first_buckets.pop())
            lst.pop()


DFS(0)
print(len(s))