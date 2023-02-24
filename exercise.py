# complete the function below and return the reverse of the given number

def reverse():
    num = 123456789
    reverse_n = 0
    reverse_number = 0
    # add your code here
    
    while num > 0:
       n = num % 10
    #    print(n)
       reverse_number = (reverse_number * 10) +n
    #    print(reverse_number)
       num = num // 10
    #    print(num)
    #    print(reverse_number)
    
    print(reverse_number)

    return reverse_number

reverse()