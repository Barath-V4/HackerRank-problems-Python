n=int(input())
arr=list(map(int, input().split()))
arr.sort(reverse=True)
s=set(arr)
m=max(s)
s.remove(m)
print(max(s))
