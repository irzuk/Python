
def fib_fun(num):
    nums = [0, 1]
    for i in range(2, num + 1):
        nums.append(nums[i - 1] + nums[i - 2])
    return nums

