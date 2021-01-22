n = int(input("Enter the number: "))                      
p = len(str(n))                                           
s = 0                                                     
k = n                                                     
if k>0:                                                
    d = k%10                                              
    s = s + (d**p)                                        
    k = k//10
else :
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")

if n == s:                                                
    print('{} is an Armstrong number'.format(n))          
else:                                                       
    print('{} is not an Armstrong number'.format(n))  