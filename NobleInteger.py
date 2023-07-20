'''
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.

Input 1:
A = [3, 2, 1, 3]

Input 2:
A = [1, 1, 3, 3]

Output 1:
1

Output 2:
-1
'''
array = list(map(int, input().split()))
array.sort(reverse = True)
small , noble = 0, 0
count = 0
if array[0] == 0:
    noble += 1
for i in range(1,len(array)):
    if array[i]!=array[i-1]:
        small = i
        if small == array[i]:
            noble +=1
print(-1 if noble==0 else noble)