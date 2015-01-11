class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        st = set(num)
        maxnum = 0
        for number in num:
            if number in st:
                count = 1
                left = number-1
                while left in st:
                    st.remove(left)
                    count += 1
                    left -= 1
                right = number+1
                while right in st:
                    st.remove(right)
                    count += 1
                    right += 1
                maxnum = max(maxnum,count)
        return maxnum