class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        refill = [x-y for x,y in zip(gas,cost)]
        sum = 0
        index = 0
        rest = 0
        for i,num in enumerate(refill):
            sum += num
            if sum<0:
                rest += sum
                sum = 0
                index = i+1
        if rest+sum>=0:
            return index
        return -1