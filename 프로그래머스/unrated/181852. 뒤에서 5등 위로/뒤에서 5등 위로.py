def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    lesser, equal, greater = [], [], []
    for num in arr:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    return quick_sort(lesser) + equal + quick_sort(greater)


def solution(num_list):
    answer = quick_sort(num_list)
    answer = answer[5:]
    return answer