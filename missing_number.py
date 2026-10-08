n= int(input())
arr = list(map(int,input().split()))
total = sum(arr)
sums = n*(n+1)//2
print(sums-total)