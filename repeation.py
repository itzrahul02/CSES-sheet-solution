string = input()
longest = 0
left = 0
for right in range(len(string)):
    if(string[right]!=string[left]):
        left = right
    longest = max(longest,right-left+1)

print(longest)