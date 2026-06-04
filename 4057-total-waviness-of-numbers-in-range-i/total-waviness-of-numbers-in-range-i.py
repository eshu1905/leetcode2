class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count=0
        if num2<100:
            return 0
        for i in range(num1,num2+1):
            num_str=str(i)
            n=len(num_str)
            for i in range(1,n-1):
                if int(num_str[i-1])<int(num_str[i])>int(num_str[i+1]) or int(num_str[i-1])>int(num_str[i])<int(num_str[i+1]):
                    count+=1
        return count
        

        