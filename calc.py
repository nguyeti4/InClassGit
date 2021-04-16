def calc(a,b):
    summ = a + b
    difference = a-b
    multiply = a*b
    divide = a/b
    
    array = [summ,difference,multiply,divide]
    
    #calc sum of the list
    total = 0
    for x in array:
        total += x
    
    #print the sum
    print(total)
       
        
 
