def list_divisors(num):
    #empty list
    list = []
    #iterate through numbers 1->num
    for i in range(1,num+1):
        if num % i == 0:
            list.append(i)
    #print(list)
    for i in list:
        

list_divisors(42)