class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        nearsum = num[0]+num[1]+num[2]
        for i,number in enumerate(num):
            start = i+1
            end = len(num)-1
            while start<end:
                temp = num[start]+num[end]+number
                if abs(target-temp)<abs(nearsum-target):
                    nearsum = temp
                if target>temp:
                    start += 1
                else:
                    end -= 1
        return nearsum