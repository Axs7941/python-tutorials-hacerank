

def isPrime(n):
    if n <=1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True 

num_test_cases = int(input())
for i in range(num_test_cases):
    n= int(input())
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")
        
        

# Objective:
# Today we will learn about running time, also known as time complexity. Check out the Tutorial tab for learning materials and an instructional video.
# Task:
# A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, , determine and print whether it is  or .

