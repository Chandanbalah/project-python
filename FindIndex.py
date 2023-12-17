in_elements= int(input())
nums=[]
res_temp=0
for n in range(in_elements):
    numstemp=int(input())
    nums.append(numstemp)
print('nums',nums)
target = int(input())
print('target',target)
for i in nums:
    if i == target:
        print('output',nums.index(i))
        break
    elif target <i:
        print('output',nums.index(i))
        break
    elif target>max(nums):
        print('output',len(nums))
        break
    else:
        print('index out of range')
