def find_prime(number):
    for i in range(2,number):
        if(number%i==0):
            return 0
    return 1
        
def largest_prime_factor(num):
    for i in range(num-1,1,-1):
        if(num%i==0 and find_prime(i)==1):
            print(i)
            break

num=int(input())
largest_prime_factor(num)
