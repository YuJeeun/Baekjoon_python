def solution(nums):
    answer = 0
    n = set(nums)
    test = len(nums)//2

    if len(n) < test:
        return len(n)
    else:
        return test