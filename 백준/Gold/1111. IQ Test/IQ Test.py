import sys
input = sys.stdin.readline
#아이디어: 수열이 3개 부터는 정확한 점화식의 계수를 구할 수 있다. 이외의 경우는 예외처리 필요
#n 입력받기
n = int(input())
#수들 입력받기
nums = list(map(int,input().split()))
if len(nums) == 1:
    print('A')
elif len(nums) == 2 and nums[0] == nums[1]:
    print(f'{nums[0]}')
elif len(nums) == 2:
    print('A')
else:
    if nums[0] == nums[1]:
        if all(num == nums[0] for num in nums):
            print(f'{nums[0]}')
        else:
            print('B')
    else:
        if nums[1] == 0:
            b = nums[2]
            a = -b // nums[0]
        else: 
            b = (nums[1]**2-nums[0]*nums[2]) // (nums[1] - nums[0])
            a = (nums[2] - b) // nums[1]
        if all(nums[i] == nums[i-1]*a + b for i in range(1,len(nums))):
            print(f'{nums[-1]*a + b}')
        else:
            print('B')