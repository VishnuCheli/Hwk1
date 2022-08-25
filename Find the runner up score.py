if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr_sorted = sorted(list(arr), reverse=True)
    max_v=max(arr_sorted)
    
    for x in (arr_sorted):
        if(x == max_v):
            continue
        else:
            max_second = x
            break
    print(max_second)