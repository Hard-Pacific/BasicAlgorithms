class Fibonacci():
    def generate(self, n):
        nums = [1, 1]
        c = 0
        while nums[c] + nums[c+1] < n:
            nums.append(nums[c] + nums[c+1])
            c += 1
        return nums
    
    