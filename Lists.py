if __name__ == '__main__':
    N = int(input())
    
    split_arr = []
    arr =[]
    
    for i in range(N):
        x = input().split()
        split_arr.append(x)

    for i in range(len(split_arr)):
        if split_arr[i][0] == 'insert':
            x = int(split_arr[i][1])
            y = int(split_arr[i][2])
            arr.insert(x,y)
        elif split_arr[i][0]=='print':
            print(arr)
        elif split_arr[i][0]=='remove':
            arr.remove(int(split_arr[i][1]))
        elif split_arr[i][0] =='append':
            arr.append(int(split_arr[i][1]))
        elif split_arr[i][0]=='sort':
            arr.sort()
        elif split_arr[i][0]=='pop':
            arr.pop()
        elif split_arr[i][0]=='reverse':
            arr.reverse()
            