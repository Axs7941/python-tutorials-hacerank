class Calculator:
    def power(self,n,p):
        if n<0 or p<0:
            raise Exception("n and p should be non-negative");
        else:
            return  pow(n,p)

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   


# Objective:
# Yesterday's challenge taught you to manage exceptional situations by using try and catch blocks. In today's challenge, you will practice throwing and propagating an exception. Check out the Tutorial tab for learning materials and an instructional video.

# Task:
# Write a Calculator class with a single method: int power(int,int). The power method takes two integers,  and , as parameters and returns the integer result of . If either  or  is negative, then the method must throw an exception with the message: n and p should be non-negative.