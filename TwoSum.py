in_elements= int(input())
nums=[]
res_temp=0
for n in range(in_elements):
    numstemp=int(input())
    nums.append(numstemp)
print('nums',nums)
target = int(input())
print('target',target)

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print(i,j)
        else:
            print('else')
